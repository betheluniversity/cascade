from copy import *
import datetime
from xml.etree import ElementTree

# TODO: Multiselect and checkboxes will need extra work if NONE is found
def update(search_list, key, value):
    """ Updates a specified key-value pair within an Asset

    :param search_list: The Asset, Metadata, or Structured Metadata to update
    :param key: The key being updated
    :param value: The new value to be assigned to this key
    :return: Tuple (Message, success)
    """

    # get the element to update
    returned_search_list = find(search_list, key)

    # if there is ever a list, then it is about to all get deleted and overwritten.
    # therefore, it is fine to just grab the first element and move on
    # The functions prior to this should never return an empty list, it should return None instead.
    if type(returned_search_list) == list:
        returned_search_list = returned_search_list[0]

    if type(value) == list:
        # get the parent element so that we can delete all applicable children
        parent_element = __search_for_element__(search_list, key, True)

        if parent_element is not None:

            new_elements = []
            if len(value) == 0:
                temp_element = deepcopy(find(parent_element, key))
                temp_element = clear_element_values(temp_element)
                new_elements.append(temp_element)
            else:
                # create a new element to append later
                for single_value in value:
                    new_elements.append(deepcopy(update(parent_element, key, single_value)))

            # gather indices to delete
            indexes_to_remove = []
            for index, element in enumerate(parent_element):
                if 'name' in element and element['name'] == key:
                    indexes_to_remove.append(index)
                elif 'identifier' in element and element['identifier'] == key:
                    indexes_to_remove.append(index)

            # delete the old ones
            for index in reversed(indexes_to_remove):
                del parent_element[index]

            # append the new elements back on (these were created above)
            for new_element in new_elements:
                parent_element.append(new_element)

        return returned_search_list

    if returned_search_list is None:
        return None

    # dynamic metadata
    if 'name' in returned_search_list and returned_search_list['name'] == key:
        new_value_array = []
        if type(value) is list:
            for child in value:
                new_value_array.append({'value': child})
        else:
            new_value_array.append({'value': value})

        # build structure, if it doesn't already exist
        # todo: shorten up this logic -- simplify
        if 'fieldValues' in returned_search_list and 'fieldValue' in returned_search_list['fieldValues']:
            returned_search_list['fieldValues']['fieldValue'] = new_value_array
        else:
            returned_search_list['fieldValues'] = {'fieldValue': new_value_array}
        return returned_search_list

    # basic metadata
    elif key in returned_search_list:
        returned_search_list[key] = value
        return returned_search_list

    # structured data
    elif returned_search_list.get('identifier') == key:

        if returned_search_list['type'] == 'text':
            # get the type of content xml
            if '::CONTENT-XML-CHECKBOX::' in str(returned_search_list.get('text', '')):
                content_xml_type = '::CONTENT-XML-CHECKBOX::'
            elif '::CONTENT-XML-SELECTOR::' in str(returned_search_list.get('text', '')):
                content_xml_type = '::CONTENT-XML-SELECTOR::'
            else:
                content_xml_type = None

            # checkbox - list
            if type(value) is list:
                new_value = ''
                for item in value:
                    new_value += content_xml_type + item
            # checkbox - single value
            elif content_xml_type:
                new_value = content_xml_type + value
            # normal text
            else:
                new_value = value

            returned_search_list['text'] = new_value
            return returned_search_list

        # groups
        elif returned_search_list['type'] == 'group':
            for subkey, subvalue in value.items():
                update(returned_search_list, subkey, subvalue)

            return returned_search_list

        # assets
        elif returned_search_list['type'] == 'asset':
            if value is None:
                return None
            asset_type = returned_search_list['assetType']

            # null out the id and path
            returned_search_list[asset_type + 'Id'] = ''
            returned_search_list[asset_type + 'Path'] = ''

            # check if id or path is value
            if '/' in value:
                returned_search_list[asset_type + 'Path'] = value
            else:
                returned_search_list[asset_type + 'Id'] = value

            return returned_search_list

        else:
            return None
    else:
        return None


# This is currently used to update md sets. Could be made more robust in the future
def update_metadata_set(search_list, key, value, default=None):
    """ Updates a specified key-value pair within an Asset

    :param search_list: The Asset, Metadata, or Structured Metadata containing the key-value to update
    :param key: The key being updated
    :param value: The new value to be assigned to this key
    :param default: The default value for this metadata set is true
    :return: Tuple (Message, success)
    """
    # get the element to update
    returned_search_list = __search_for_element__(search_list, key)

    if returned_search_list is None:
        return None

    # possible values
    if 'name' in returned_search_list and returned_search_list['name'] == key and 'fieldType' != 'text':
        new_value_array = []
        if type(value) is list:
            for child in value:
                # todo make this into a method
                if child == default:
                    new_value_array.append({'value': child, 'selectedByDefault': True})
                else:
                    new_value_array.append({'value': child})
        else:
            # todo make this into a method
            if value == default:
                new_value_array.append({'value': value, 'selectedByDefault': True})
            else:
                new_value_array.append({'value': value})

        # build structure, if it doesn't already exist
        # todo: shorten up this logic -- simplify
        if 'possibleValues' in returned_search_list and 'possibleValue' in returned_search_list['possibleValues']:
            returned_search_list['possibleValues']['possibleValue'] = new_value_array
        else:
            returned_search_list['possibleValues'] = {'possibleValue': new_value_array}
        return key

    # basic values
    elif key in returned_search_list:
        returned_search_list[key] = value
        return key

    else:
        return None


# This is currently used to update data definitions. Could be made more robust in the future
def update_data_definition(search_xml, key, value, default=None):
    return_key = False
    if 'dataDefinition' in search_xml:
        xml = search_xml['dataDefinition']['xml']
    else:
        return None

    search_xml_in_json = ElementTree.fromstring(xml)

    for child in search_xml_in_json.findall('.//text'):
        if child.get('identifier') == key:
            if child.get('type') == 'checkbox':
                field_type = 'checkbox-item'
            elif child.get('type') == 'dropdown':
                field_type = 'dropdown-item'
            elif child.get('type') == 'radiobutton':
                field_type = 'radio-item'
            elif child.get('type') == 'multi-selector':
                field_type = 'selector-item'
            else:
                continue

            # This process is to be able to delete elements without changing the array size
            # gather elements to remove
            indexes_to_remove = []
            for index, element in enumerate(child):
                indexes_to_remove.append(element)
            # remove the elements
            for element in indexes_to_remove:
                child.remove(element)

            # add all
            for index, single_value in enumerate(value):
                # todo make this into a method
                if single_value == default:
                    child.append(ElementTree.Element(field_type, {'value': single_value.replace(' & ', ' &amp; '), 'selectedByDefault': True}))
                else:
                    child.append(ElementTree.Element(field_type, {'value': single_value.replace(' & ', ' &amp; ')}))

            return_key = True
            break


    if return_key:
        search_xml['dataDefinition']['xml'] = ElementTree.tostring(search_xml_in_json)
        return key
    else:
        return None


# returns the value of the element or the full element
def find(search_list, key, return_full_element=True):
    """ Looks for a given key

    :param search_list: The Asset, Metadata, or Structured Metadata to update ('the haystack')
    :param key: The key being searched for ('the needle')
    :param return_full_element: (optional) If false, returns the value or values associated with the key.
    :return: The full element (unless otherwised specified)
    """
    # Get the element
    returned_search_list = __search_for_element__(search_list, key)

    # return the element
    if return_full_element:
        return returned_search_list

    array_to_return = []
    element = returned_search_list

    if hasattr(element, 'keys') and key in element.keys():
        array_to_return.append(element[key])
    else:
        try:
            # dynamic md
            if 'fieldValues' in element:
                temp_array = []
                for item in element['fieldValues']['fieldValue']:
                    temp_array.append(item['value'])
                array_to_return.append(temp_array)

            # text fields, checkboxes, and multiselects
            elif element['type'] == 'text':
                # this is an extra check for checkbox. It will return the text or an array of checkbox values
                if '::CONTENT-XML-CHECKBOX::' in str(element['text']):
                    value_of_text = str(element['text']).split('::CONTENT-XML-CHECKBOX::')
                elif '::CONTENT-XML-SELECTOR::' in str(element['text']):
                    value_of_text = str(element['text']).split('::CONTENT-XML-SELECTOR::')
                else:
                    value_of_text = str(element['text'])

                if len(value_of_text) == 0:
                    pass
                elif len(value_of_text) == 1:
                    array_to_return.append(value_of_text[0])
                else:
                    array_to_return.append(value_of_text)

            # groups
            elif element['type'] == 'group':
                array_to_return.append(element['structuredDataNodes']['structuredDataNode'])

            # assets
            elif element['type'] == 'asset':
                array_to_return.append(element)

            # it should only get here if new types are added
            else:
                print('ERROR: need to add more checks here!')
                print(element)
        except:
            pass

    return __return_formated_array__(array_to_return)


# an internal search to get the right element
# can only be called on the top level asset, top level metadata, or the top level structured data
def __search_for_element__(search_list, key, find_parent_element=False):
    # basic MD values
    if hasattr(search_list, 'keys') and key in search_list.keys():
        return search_list
    # dynamic MD fields
    elif hasattr(search_list, 'keys') and 'name' in search_list.keys() and search_list['name'] == key:
        return search_list
    # DS values
    elif hasattr(search_list, 'get') and search_list.get('identifier') == key:
        return search_list

    found_array = []

    # loop over the list
    for child in search_list:
        # basic MD values
        if hasattr(child, 'keys') and key in child.keys():
            if find_parent_element:
                return search_list
            else:
                return child
        # dynamic MD fields
        elif hasattr(child, 'keys') and 'name' in child.keys() and child['name'] == key:
            if find_parent_element:
                return search_list
            else:
                return child
        # DS values
        elif hasattr(child, 'get') and child.get('identifier') == key:
            if find_parent_element:
                return search_list
            else:
                return child

        if hasattr(search_list, 'get'):
            if type(search_list.get(child)) == dict:
                found = __search_for_element__(search_list.get(child), key, find_parent_element)

                if found:
                    if find_parent_element:
                        return found
                    else:
                        found_array.append(found)

            elif type(search_list.get(child)) == list:
                for item in search_list.get(child):
                    found = __search_for_element__(item, key, find_parent_element)

                    if found:
                        if find_parent_element:
                            return search_list.get(child)
                        else:
                            found_array.append(found)

    return __return_formated_array__(found_array)


# return an array that can handle lists only when needed
def __return_formated_array__(array):
    if len(array) == 0:
        return None
    elif len(array) == 1:
        return array[0]
    else:
        return array

def clear_element_values(element):
    # group
    if 'type' in element and element.get('type') == 'group':
        parent_element = element['structuredDataNodes']['structuredDataNode']
        for child in parent_element:
            if 'text' in child:
                child['text'] = ''
            elif 'type' in child and child.get('type') == 'asset':
                asset_type = child.get('assetType')
                child[asset_type + 'Id'] = ''
                child[asset_type + 'Path'] = ''
            elif 'type' in child and child.get('type') == 'group':
                child = clear_element_values(child)
        return element
    # dynamic md
    elif 'fieldValues' in element:
        element['fieldValues']['fieldValue'] = []
        element['fieldValues']['fieldValue'].append({
            'value': ''
        })
        return element
    else:
        return None


# python3 doesn't handle bytes comparison with str well.
# https://stackoverflow.com/questions/33137741/fastest-way-to-convert-a-dicts-keys-values-from-bytes-to-str-in-python3
def convert_asset(data):
  if isinstance(data, bytes):                                       return data.decode()
  if isinstance(data, bool) or isinstance(data, datetime.date):     return data
  if isinstance(data, (str, int)):                                  return str(data)
  if isinstance(data, dict):                                        return dict(map(convert_asset, data.items()))
  if isinstance(data, tuple):                                       return tuple(map(convert_asset, data))
  if isinstance(data, list):                                        return list(map(convert_asset, data))
  if isinstance(data, set):                                         return set(map(convert_asset, data))

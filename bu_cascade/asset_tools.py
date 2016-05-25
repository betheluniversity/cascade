__author__ = 'ces55739'

from copy import *

def update(search_list, key, value):
    # get the element to update
    returned_search_list = find(search_list, key, True)

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
            # create a new element to append later
            for single_value in value:
                new_elements.append(deepcopy(update(parent_element, key, single_value)))

            # gather indices to delete
            indexes_to_remove = []
            for index, element in enumerate(parent_element['structuredDataNodes']['structuredDataNode']):
                if element['identifier'] == key:
                    indexes_to_remove.append(index)

            # delete the old ones
            for index in reversed(indexes_to_remove):
                del parent_element['structuredDataNodes']['structuredDataNode'][index]

            # append the new elements back on (these were created above)
            for new_element in new_elements:
                parent_element['structuredDataNodes']['structuredDataNode'].append(new_element)

        return returned_search_list

    if returned_search_list is None:
        return None

    # dynamic metadata
    if 'fieldValues' in returned_search_list.keys() and returned_search_list['name'] == key:
        new_value_array = []
        if type(value) is list:
            for item in value:
                new_value_array.append({'value': item})
        else:
            new_value_array.append({'value': value})
        returned_search_list['fieldValues']['fieldValue'] = new_value_array
        return returned_search_list

    # basic metadata
    elif key in returned_search_list:
        returned_search_list[key] = value
        return returned_search_list

    # structured data
    elif returned_search_list.get('identifier') == key:

        if returned_search_list['type'] == 'text':
            # get the type of content xml
            if '::CONTENT-XML-CHECKBOX::' in returned_search_list.get('text',''):
                content_xml_type = '::CONTENT-XML-CHECKBOX::'
            elif '::CONTENT-XML-SELECTOR::' in returned_search_list.get('text',''):
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


# returns the value of the element or the full element
def find(search_list, key, return_full_element=True):
    # Get the element
    returned_search_list = __search_for_element__(search_list, key)

    # return the element
    if return_full_element:
        return returned_search_list

    array_to_return = []

    for el in returned_search_list:
        if hasattr(el, 'keys') and key in el.keys():
            array_to_return.append(el[key])
        else:
            try:
                # dynamic md
                if 'fieldValues' in el:
                    temp_array = []
                    for item in el['fieldValues']['fieldValue']:
                        temp_array.append(item['value'])
                    array_to_return.append(temp_array)

                # text fields, checkboxes, and multiselects
                elif el['type'] == 'text':
                    # this is an extra check for checkbox. It will return the text or an array of checkbox values
                    if '::CONTENT-XML-CHECKBOX::' in el['text']:
                        value_of_text = el['text'].split('::CONTENT-XML-CHECKBOX::')
                    elif '::CONTENT-XML-SELECTOR::' in el['text']:
                        value_of_text = el['text'].split('::CONTENT-XML-SELECTOR::')
                    else:
                        value_of_text = el['text']

                    if len(value_of_text) == 0:
                        pass
                    elif len(value_of_text) == 1:
                        array_to_return.append(value_of_text[0])
                    else:
                        array_to_return.append(value_of_text)

                # groups
                elif el['type'] == 'group':
                    array_to_return.append(el['structuredDataNodes']['structuredDataNode'])

                # assets
                elif el['type'] == 'asset':
                    asset_type = el['assetType']
                    array_to_return.append(el)

                # it should only get here if new types are added
                else:
                    print 'ERROR: need to add more checks here!'
                    print el
            except:
                pass

    return __return_formated_array__(array_to_return)


# an internal search to get the right element
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
    for k in search_list:
        if type(search_list.get(k)) == dict:
            found = __search_for_element__(search_list.get(k), key)

            if found:
                if find_parent_element:
                    return search_list
                else:
                    found_array.append(found)

        elif type(search_list.get(k)) == list:
            for item in search_list.get(k):
                found = __search_for_element__(item, key)

                if found:
                    if find_parent_element:
                        return search_list
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
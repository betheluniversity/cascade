__author__ = 'ces55739'

# Todo: can this handle 'multiple' elements
def update(search_list, key, value):
    returned_search_list = find(search_list, key, True)

    if type(returned_search_list) == list:
        returned_search_list = returned_search_list[0]

    # todo: update a list
    if type(value) == list:
        # delete all but 1.
        parent_element = __search_for_parent_element__(search_list, key)
        print parent_element
        if parent_element is not None:

            # Delete elements
            new_parent_element = parent_element['structuredDataNodes']['structuredDataNode']
            matched_first = False

            for index, element in enumerate(new_parent_element):
                if element['identifier'] == key:
                    if matched_first:
                        new_parent_element.remove(element)
                    matched_first = True

            # print parent_element
            new_elements = []

            # create each new element todo: reverse this
            for single_value in value:
                print key, single_value
                # Todo: this is where it is broken
                # new_elements.append( update(new_parent_element, key, single_value) )
            print new_elements

            # append each back to the main element
            # for new_element in new_elements:
            #     print new_element
                # returned_search_list.append(new_element)

        return returned_search_list

    if returned_search_list is None:
        return None

    # complex metadata
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
    elif returned_search_list.get(key):
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
                # Checkboxes are considered 'text'
                if 'fieldValues' in el:
                    temp_array = []
                    for item in el['fieldValues']['fieldValue']:
                        temp_array.append(item['value'])
                    array_to_return.append(temp_array)

                elif el['type'] == 'text':
                    # Todo: add the extra check for multiselect! (it is done above in the update method)
                    # this is an extra check for checkbox. It will return the text or an array of checkbox values
                    value_of_text = el['text'].split('::CONTENT-XML-CHECKBOX::')

                    if len(value_of_text) == 0:
                        pass
                    elif len(value_of_text) == 1:
                        array_to_return.append(value_of_text[0])
                    else:
                        array_to_return.append(value_of_text)



                elif el['type'] == 'group':
                    array_to_return.append(el['structuredDataNodes']['structuredDataNode'])

                elif el['type'] == 'asset':
                    asset_type = el['assetType']
                    array_to_return.append(el)
                else:
                    print 'ERROR: need to add more checks here!'
                    print el
            except:
                pass

    if len(array_to_return) == 0:
        return None
    elif len(array_to_return) == 1:
        return array_to_return[0]
    else:
        return array_to_return


# an internal search to get the right element
def __search_for_element__(search_list, key):

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
                found_array.append(found)
        elif type(search_list[k]) == list:
            for item in search_list.get(k):
                found = __search_for_element__(item, key)
                if found:
                    found_array.append(found)

    if len(found_array) == 0:
        return None
    elif len(found_array) == 1:
        return found_array[0]
    else:
        return found_array


# an internal search to get the right element
def __search_for_parent_element__(search_list, key):
    # basic MD values
    if hasattr(search_list, 'keys') and key in search_list.keys():
        return search_list
    # dynamic MD fields
    elif hasattr(search_list, 'keys') and 'name' in search_list.keys() and search_list['name'] == key:
        return search_list
    # DS values
    elif hasattr(search_list, 'get') and search_list.get('identifier') == key:
        return search_list

    # loop over the list
    for k in search_list:
        if type(search_list.get(k)) == dict:
            found = __search_for_parent_element__(search_list.get(k), key)
            if found:
                return search_list
        elif type(search_list[k]) == list:
            for item in search_list.get(k):
                found = __search_for_parent_element__(item, key)
                if found:
                    return search_list


# deletion is used by the update method. in order to add new elements, we need to delete all but 1, then copy.
def __delete_all_but_first__(search_list, key):
    # skip the first element, then delete the rest
    for index, val in enumerate(search_list):
        if index != 0:
            search_list.__delitem__(index)

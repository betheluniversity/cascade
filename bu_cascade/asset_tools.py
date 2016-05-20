__author__ = 'ces55739'


def update(search_list, key, value):
    returned_search_list = find(search_list, key, True)

    if returned_search_list is None:
        return None

    # complex metadata
    if 'fieldValues' in returned_search_list.keys() and returned_search_list['name'] == key:
        print 'test'
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
            if '::CONTENT-XML-CHECKBOX::' in returned_search_list['text']:
                content_xml_type = '::CONTENT-XML-CHECKBOX::'
            elif '::CONTENT-XML-SELECTOR::' in returned_search_list['text']:
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

        # elif returned_search_list['type'] == 'group':
        #     return returned_search_list['structuredDataNodes']['structuredDataNode']

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

    if hasattr(returned_search_list, 'keys') and key in returned_search_list.keys():
        return returned_search_list[key]
    else:
        try:
            # Checkboxes are considered 'text'
            if 'fieldValues' in returned_search_list:
                temp_array = []
                for item in returned_search_list['fieldValues']['fieldValue']:
                    temp_array.append(item['value'])
                return temp_array

            elif returned_search_list['type'] == 'text':
                # this is an extra check for checkbox. It will return the text or an array of checkbox values
                return returned_search_list['text'].split('::CONTENT-XML-CHECKBOX::')

            elif returned_search_list['type'] == 'group':
                return returned_search_list['structuredDataNodes']['structuredDataNode']

            elif returned_search_list['type'] == 'asset':
                asset_type = returned_search_list['assetType']
                return returned_search_list

            else:
                print 'ERROR: need to add more checks here!'
                print returned_search_list
        except:
            return None


# an internal search to get the right element
def __search_for_element__(search_list, key):
    # basic MD values
    if key in search_list.keys():
        return search_list
    # dynamic MD fields
    elif 'name' in search_list.keys() and search_list['name'] == key:
        return search_list
    # DS values
    elif search_list.get('identifier') == key:
        return search_list

    # loop over the list
    for k in search_list:
        if type(search_list[k]) == dict:
            found = __search_for_element__(search_list[k], key)
            if found:
                return found
        elif type(search_list[k]) == list:
            for item in search_list[k]:
                found = __search_for_element__(item, key)
                if found:
                    return found

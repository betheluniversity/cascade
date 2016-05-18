__author__ = 'ces55739'


# Todo: Eric's new stuff can go here?
class AssetTools():

    # def __init__(self, asset):
    #     self.asset = asset

    # def get_asset(self):
    #     return self.asset

    # only useful for finding structured nodes
    def find(self, key, asset_structure):
        if asset_structure is None:
            asset_structure = self.get_asset()

        match = False
        if 'identifier' in asset_structure and asset_structure['identifier'] == key:
            match = AssetTools(asset_structure)
        else:
            for node in asset_structure:
                if isinstance(asset_structure, list) and (isinstance(node, dict) or isinstance(node, list)):
                    match = self.find(key, node)
                elif isinstance(asset_structure, dict) and (isinstance(asset_structure[node], dict) or isinstance(asset_structure[node], list)):
                    match = self.find(key, asset_structure[node])

                if match is not False:
                    return match

        return match


    def set(self, value):
        asset = self.asset
        type = asset['type']
        if type == "text":
            asset['text'] = value
            return True
        elif type == "asset":
            asset_type = asset.asset_type

            ## Todo: blocks/pages/files all have Id's and Path's to set.
            # either take in path or id.
            # use the path or id to set the id or path?
            # might be a little tricky, but it probably makes the most sense.
            # asset[asset_type+"Id"] =
            # asset[asset_type+"Path"] =

        ## Todo: do we care about group?
        # elif type == "group":
        else:
            return False


    ## Todo: Needs to be updated or merged with find() above ^^. I think having a separate function will be more helpful.
    ## only useful for finding structured nodes
    def find_all(self, key, asset_structure=None):
        if asset_structure is None:
            asset_structure = self.get_asset()

        matches = []
        if 'identifier' in asset_structure and asset_structure['identifier'] == key:
            matches.append(AssetTools(asset_structure))
        else:
            for node in asset_structure:
                result = []
                if isinstance(asset_structure, list) and (isinstance(node, dict) or isinstance(node, list)):
                    result = self.find_all(key, node)
                elif isinstance(asset_structure, dict) and (isinstance(asset_structure[node], dict) or isinstance(asset_structure[node], list)):
                    result = self.find_all(key, asset_structure[node])
                if result != []:
                    matches.append(result)

        return matches


    def find_md_field(self, key, newValues=None):
        asset_structure = self.get_asset()

        ## normal md values (title, teaser, description, etc. )
        if key in asset_structure:
            if newValues is not None:
                asset_structure[key] = newValues
            # return asset_structure[key]
        else: ## dynamic values
            for node in asset_structure['dynamicFields']['dynamicField']:
                if node['name'] == key:
                    if newValues:
                        node['fieldValues']['fieldValue'] = []
                        for value in newValues:
                            value_string = {'value': str(value)}
                            node['fieldValues']['fieldValue'].append(value_string)

                    value_list = []
                    for value in node['fieldValues']['fieldValue']:
                        value_list.append(value['value'])
                    return str(value_list)
        return False
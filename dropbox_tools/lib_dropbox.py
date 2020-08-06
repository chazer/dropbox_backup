import json
import urllib.request


class Dropbox:

    def __init__(self, token):
        self.token = token

    def read_entries(self, doc):
        if doc['entries']:
            for entry in doc['entries']:
                item = {
                    'id': None,
                    '.tag': None,
                    'path_display': None,
                    'name': None,
                    'path_lower': None,
                    'is_downloadable': None,
                    'size': None,
                    'client_modified': None,
                    'server_modified': None,
                    '.tag': None,
                    'content_hash': None,
                    'rev': None,
                    'path_lower': None,
                }
                item.update(entry)
                yield item

    def dropbox_list_folder(self, path=""):
        def read_cursor_response(doc):
            items = self.read_entries(doc)
            for item in items:
                yield item
            has_more = doc['has_more']
            # TODO
            pass

        data = {'path': path,
                'recursive': False,
                'include_media_info': False,
                'include_deleted': False,
                'include_has_explicit_shared_members': False,
                'include_mounted_folders': True,
                'include_non_downloadable_files': True,
               }
        req = urllib.request.Request(
            "https://api.dropboxapi.com/2/files/list_folder",
            method="POST",
            headers={'content-type': 'application/json',
                     'authorization': "Bearer {}".format(self.token),
                    },
            data=json.dumps(data).encode('utf8'),
        )
        response = urllib.request.urlopen(req)
        resp_doc_json = response.read().decode('utf8')
        resp_doc = json.loads(resp_doc_json)
        return read_cursor_response(resp_doc)


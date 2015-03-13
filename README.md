# MDID-(re)Search

An investigaiton into ripping out rooibos.solr and replace it with search provided by django-haystack 

### Why?

TO give some more flexibility of search providers. We had hoped it might also make managing the search index a bit better, but alas. 

# NOTE - still working it out, this may not work as committed

## current status

```
./manage.py haystack_info

Number of handled 3 index(es).
  - Model: FieldValue by Index: <rooibos.apps.mdid-search.search_indexes.FieldValueIndex object at 0x108d6c530>
  - Model: Record by Index: <rooibos.apps.mdid-search.search_indexes.RecordIndex object at 0x108d6c600>
  - Model: Field by Index: <rooibos.apps.mdid-search.search_indexes.FieldIndex object at 0x108d6c4c8>
```

`./manage.py build_solr_schema`

see [generated_schema.xml](generated_schema.xml)

## Checking it out

`pip install --upgrade django-haystack`
`pip install --upgrade pysolr`

in $MDIDROOT/rooibos/apps

`git clone 

in $MDIDROOT/config/settings_local.py

```python
INSTALLED_APPS = (
    'haystack',
    'rooibos.apps.mdid-search',
)

# assuming you're using solr (solr4 may be required)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}

```
import datetime
from haystack import indexes
from rooibos.data.models import Record, Field, FieldValue


class RecordIndex(indexes.SearchIndex, indexes.Indexable):
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    title = indexes.CharField(model_attr='title', document=True, use_template=True)
    created = indexes.DateTimeField(model_attr='created', faceted=True)
    modified = indexes.DateTimeField(model_attr='modified', faceted=True)
    source = indexes.CharField(model_attr='source')

    def get_model(self):
        return Record

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

    # TODO: not sure what (if anything) to do with FKs - and I don't the think the rest need to be indexed
    #copied from rooibos.data.Record
    # name = indexes.CharField()
    # source = indexes.CharField()
    # manager = indexes.CharField()
    # next_update = indexes.DateTimeField()
    ## parent = models.ForeignKey('self', null=True, blank=True)
    ## owner = models.ForeignKey(User, null=True, blank=True)


class FieldIndex(indexes.SearchIndex, indexes.Indexable):
    label = indexes.CharField(model_attr='label')

    def get_model(self):
        return Field

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())


class FieldValueIndex(indexes.SearchIndex, indexes.Indexable):
    record = indexes.CharField(model_attr='record')
    field = indexes.CharField(model_attr='field')
    label = indexes.CharField(model_attr='label')
    value = indexes.CharField(model_attr='value')

    def get_model(self):
        return FieldValue

    def prepare_record(self, obj):
        return obj.record.name

    def prepare_label(self, obj):
        return obj.field.label

    def prepare_field(self, obj):
        return obj.field.name

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

    # TODO: figure out what other values need to be indexed
 #copied from rooibos.data.FieldValue
    # refinement = models.CharField(max_length=100, null=True, blank=True)
    # owner = models.ForeignKey(User, null=True, blank=True)
    # label = models.CharField(max_length=100, null=True, blank=True)
    # hidden = models.BooleanField(default=False)
    # order = models.IntegerField(default=0)
    # group = models.IntegerField(null=True, blank=True)
    # index_value = models.CharField(max_length=32, db_index=True)
    # date_start = models.DecimalField(null=True, blank=True, max_digits=12, decimal_places=0)
    # date_end = models.DecimalField(null=True, blank=True, max_digits=12, decimal_places=0)
    # numeric_value = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    # language = models.CharField(max_length=5, null=True, blank=True)
    # context_type = models.ForeignKey(ContentType, null=True, blank=True)
    # context_id = models.PositiveIntegerField(null=True, blank=True)
    # context = generic.GenericForeignKey('context_type', 'context_id')

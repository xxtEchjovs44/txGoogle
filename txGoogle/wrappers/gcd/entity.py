'''
Created on Oct 21, 2014

@author: sjuul
'''
from txGoogle.wrappers.gcd import GcdObjectWithApiBackReference
from txGoogle.wrappers.gcd import PropertyValue
from txGoogle.wrappers.gcd import Key


class Entity(GcdObjectWithApiBackReference):

    def __init__(self, dct=None, fromSerialized=False, key=None):
        self.key = None
        if dct is None:
            dct = {}
        self.properties = {}
        if fromSerialized:
            for ky, vl in dct.get('properties', {}).iteritems():  # queries can result in entity with only a key property
                if ky == 'probes':
                    print vl
                if 'indexed' in vl:
                    indexed = vl['indexed']
                    vl = vl.copy()  # take a copy so that we can remove 'indexed'
                    del vl['indexed']
                else:
                    indexed = None
                if vl:
                    firstKey = next(iter(vl))
                    self.properties[ky] = PropertyValue(vl[firstKey], valueKind=firstKey, indexed=indexed, fromSerialized=fromSerialized)
                else:
                    self.properties[ky] = PropertyValue(None, valueKind='None', fromSerialized=fromSerialized)
            if 'key' in dct:
                self.key = Key(dct['key'])
        else:
            if 'ks' in dct:
                self.key = Key(dct.pop('ks'))
            for ky, vl in dct.iteritems():
                if not isinstance(vl, PropertyValue):
                    # it is better to create property values in advance, this way you can force properties to be indexed or not
                    vl = PropertyValue(vl, valueKind=None, fromSerialized=fromSerialized)
                self.properties[ky] = vl
        if key:
            self.key = key

    @property
    def kind(self):
        if self.key.path:
            return self.key.path[-1].kind

    @property
    def name(self):
        if self.key.path:
            return self.key.path[-1].name

    def toValue(self):
        dct = {ky: vl.toValue() for ky, vl in self.properties.iteritems()}
        dct['ks'] = self.ks
        return dct

    def toDict(self):
        raise Exception('Deprecated')

    def __getitem__(self, key):
        val = self.properties.get(key)
        if val is None:
            return None
        return val.value

    def iteritems(self):
        for ky, vl in self.properties.iteritems():
            yield ky, vl.toValue()

    def __setitem__(self, key, value):
        return self.setProperty(key, value)

    def setProperty(self, key, value, valueKind=None, indexed=None):
        self.properties[key] = PropertyValue(value, valueKind=valueKind, indexed=indexed)

    def getProperty(self, key, default=None):
        if key in self.properties:
            return self.properties[key].toValue()
        else:
            return default

    get = getProperty

    def __contains__(self, key):
        return key in self.properties

    def serialize(self, outputKey=True):
        properties = {}
        output = {
            'properties': properties
        }
        if outputKey:
            output['key'] = self.key.serialize()
        for propName, propValue in self.properties.iteritems():
            properties[propName] = propValue.serialize()
        return output

    def getKeyLen(self):
        if self.key:
            return self.key.getLen()
        return 0

    def hasKey(self):
        if not self.key:
            return False
        return self.key.getLen() > 0

    def __str__(self, *args, **kwargs):
        return str(self.toValue())

    def __repr__(self, *args, **kwargs):
        return str(self.toValue())

    @property
    def ks(self):
        if self.key:
            return self.key.ks

    def put(self):
        if self.getKeyLen() == 0:
            raise Exception('Cannot save entity without key')
        return self._globalGcdWrapper.datasets.commit(self.key.datasetId or self._defaultProjectId, upsert=[self])


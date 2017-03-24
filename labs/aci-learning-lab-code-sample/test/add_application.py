#!/usr/bin/env python
'''
Autogenerated code using webarya.py
Original Object Document Input:
{"totalCount":"1","imdata":[{"fvAp":{"attributes":{"descr":"","dn":"uni/tn-Heroes/ap-Save_The_Planet","name":"Save_The_Planet","ownerKey":"","ownerTag":"","prio":"unspecified"},"children":[{"fvAEPg":{"attributes":{"descr":"","isAttrBasedEPg":"no","matchT":"AtleastOne","name":"app","prio":"unspecified"},"children":[{"fvRsCons":{"attributes":{"prio":"unspecified","tnVzBrCPName":"sql"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-201","instrImedcy":"lazy","mode":"regular","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-201","instrImedcy":"lazy","mode":"regular","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]"}}},{"fvRsDomAtt":{"attributes":{"encap":"unknown","instrImedcy":"lazy","resImedcy":"lazy","tDn":"uni/phys-Heroes_phys"}}},{"fvRsCustQosPol":{"attributes":{"tnQosCustomPolName":""}}},{"fvRsBd":{"attributes":{"tnFvBDName":"Hero_Land"}}},{"fvRsProv":{"attributes":{"matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"power_up"}}}]}},{"fvAEPg":{"attributes":{"descr":"","isAttrBasedEPg":"no","matchT":"AtleastOne","name":"db","prio":"unspecified"},"children":[{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-202","instrImedcy":"lazy","mode":"regular","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-202","instrImedcy":"lazy","mode":"regular","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]"}}},{"fvRsDomAtt":{"attributes":{"encap":"unknown","instrImedcy":"lazy","resImedcy":"lazy","tDn":"uni/phys-Heroes_phys"}}},{"fvRsCustQosPol":{"attributes":{"tnQosCustomPolName":""}}},{"fvRsBd":{"attributes":{"tnFvBDName":"Hero_Land"}}},{"fvRsProv":{"attributes":{"matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"sql"}}}]}},{"fvAEPg":{"attributes":{"descr":"","isAttrBasedEPg":"no","matchT":"AtleastOne","name":"web","prio":"unspecified"},"children":[{"fvRsCons":{"attributes":{"prio":"unspecified","tnVzBrCPName":"sql"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-200","instrImedcy":"lazy","mode":"regular","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-200","instrImedcy":"lazy","mode":"regular","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]"}}},{"fvRsDomAtt":{"attributes":{"encap":"unknown","instrImedcy":"lazy","resImedcy":"lazy","tDn":"uni/phys-Heroes_phys"}}},{"fvRsCustQosPol":{"attributes":{"tnQosCustomPolName":""}}},{"fvRsBd":{"attributes":{"tnFvBDName":"Hero_Land"}}},{"fvRsProv":{"attributes":{"matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"web"}}}]}}]}}]}

'''

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol
from cobra.internal.codec.xmlcodec import toXMLStr
from credentials import *

# configuration variables
tenant = 'Heroes'
bridge_domain = 'Hero_Land'
application = 'Save_The_Network'
vlan1 = 'vlan-211'
vlan2 = 'vlan-212'
vlan3 = 'vlan-210'

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
polUni = cobra.model.pol.Uni('')
fvTenant = cobra.model.fv.Tenant(polUni, tenant)

# build the request using cobra syntax
fvAp = cobra.model.fv.Ap(fvTenant, ownerKey=u'', name=application, prio=u'unspecified', ownerTag=u'', descr=u'')
fvAEPg = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no', matchT=u'AtleastOne', prio=u'unspecified', name=u'app', descr=u'')
fvRsCons = cobra.model.fv.RsCons(fvAEPg, tnVzBrCPName=u'sql', prio=u'unspecified')
fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]', instrImedcy=u'lazy', encap=vlan1, descr=u'', mode=u'regular')
fvRsPathAtt2 = cobra.model.fv.RsPathAtt(fvAEPg, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]', instrImedcy=u'lazy', encap=vlan1, descr=u'', mode=u'regular')
fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg, instrImedcy=u'lazy', resImedcy=u'lazy', encap=u'unknown', tDn=u'uni/phys-Heroes_phys')
fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, tnQosCustomPolName=u'')
fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName=bridge_domain)
fvRsProv = cobra.model.fv.RsProv(fvAEPg, tnVzBrCPName=u'power_up', matchT=u'AtleastOne', prio=u'unspecified')
fvAEPg2 = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no', matchT=u'AtleastOne', prio=u'unspecified', name=u'db', descr=u'')
fvRsPathAtt3 = cobra.model.fv.RsPathAtt(fvAEPg2, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]', instrImedcy=u'lazy', encap=vlan2, descr=u'', mode=u'regular')
fvRsPathAtt4 = cobra.model.fv.RsPathAtt(fvAEPg2, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]', instrImedcy=u'lazy', encap=vlan2, descr=u'', mode=u'regular')
fvRsDomAtt2 = cobra.model.fv.RsDomAtt(fvAEPg2, instrImedcy=u'lazy', resImedcy=u'lazy', encap=u'unknown', tDn=u'uni/phys-Heroes_phys')
fvRsCustQosPol2 = cobra.model.fv.RsCustQosPol(fvAEPg2, tnQosCustomPolName=u'')
fvRsBd2 = cobra.model.fv.RsBd(fvAEPg2, tnFvBDName=bridge_domain)
fvRsProv2 = cobra.model.fv.RsProv(fvAEPg2, tnVzBrCPName=u'sql', matchT=u'AtleastOne', prio=u'unspecified')
fvAEPg3 = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no', matchT=u'AtleastOne', prio=u'unspecified', name=u'web', descr=u'')
fvRsCons2 = cobra.model.fv.RsCons(fvAEPg3, tnVzBrCPName=u'sql', prio=u'unspecified')
fvRsPathAtt5 = cobra.model.fv.RsPathAtt(fvAEPg3, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]', instrImedcy=u'lazy', encap=vlan3, descr=u'', mode=u'regular')
fvRsPathAtt6 = cobra.model.fv.RsPathAtt(fvAEPg3, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]', instrImedcy=u'lazy', encap=vlan3, descr=u'', mode=u'regular')
fvRsDomAtt3 = cobra.model.fv.RsDomAtt(fvAEPg3, instrImedcy=u'lazy', resImedcy=u'lazy', encap=u'unknown', tDn=u'uni/phys-Heroes_phys')
fvRsCustQosPol3 = cobra.model.fv.RsCustQosPol(fvAEPg3, tnQosCustomPolName=u'')
fvRsBd3 = cobra.model.fv.RsBd(fvAEPg3, tnFvBDName=bridge_domain)
fvRsProv3 = cobra.model.fv.RsProv(fvAEPg3, tnVzBrCPName=u'web', matchT=u'AtleastOne', prio=u'unspecified')


# commit the generated code to APIC
print toXMLStr(fvTenant)
c = cobra.mit.request.ConfigRequest()
c.addMo(fvTenant)
md.commit(c)

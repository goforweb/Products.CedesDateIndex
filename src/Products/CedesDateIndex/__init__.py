from Products.ATContentTypes.criteria import registerCriterion
from Products.ATContentTypes.criteria.date import ATDateCriteria
from Products.ATContentTypes.criteria.daterange import ATDateRangeCriterion
from Products.ATContentTypes.criteria.sort import ATSortCriterion

registerCriterion(ATDateCriteria, 'CedesDateIndex')
registerCriterion(ATDateRangeCriterion, 'CedesDateIndex')
registerCriterion(ATSortCriterion, 'CedesDateIndex')


# Empty on purpose
def initialize(context):
    from Products.CedesDateIndex.CedesDateIndex import CedesDateIndex
    from Products.CedesDateIndex.CedesDateIndex import manage_addCedesDateIndex
    from Products.CedesDateIndex.CedesDateIndex import manage_addCedesDateIndexForm

    context.registerClass(
        CedesDateIndex,
        permission='Add Pluggable Index',
        constructors=(manage_addCedesDateIndexForm,
                      manage_addCedesDateIndex),
        icon='www/index.gif',
        visibility=None
    )


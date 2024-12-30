from plone.dexterity.interfaces import IDexterityFTI
from zope.lifecycleevent.interfaces import IObjectAddedEvent
from zope.component import adapter
from zope.interface import Interface

@adapter(IDexterityFTI, IObjectAddedEvent)
def auto_add_volto_blocks_behaviors(fti, event):
    """
    Automatically add Volto Blocks behaviors to every new content type.
    """
    # Lista comportamentelor de activat
    behaviors_to_add = [
        'plone.restapi.behaviors.IBlocks',  # Volto Blocks
        'plone.restapi.behaviors.IBlocksEditableLayout',  # Volto Blocks (Editable Layout)
        'eea.api.layout.interfaces.IFixedLayoutBlocks',  # Blocks with fixed Layout
         'plone.app.content.interfaces.ILeadImageBehavior',  # Lead Image
            
     
    ]

    # Adaugă comportamentele lipsă
    current_behaviors = list(fti.behaviors)
    for behavior in behaviors_to_add:
        if behavior not in current_behaviors:
            current_behaviors.append(behavior)
    
    fti.behaviors = tuple(current_behaviors)
    fti._p_changed = True  # Marchez obiectul ca modificat
    print(f"Behaviors {', '.join(behaviors_to_add)} added to {fti.getId()}")

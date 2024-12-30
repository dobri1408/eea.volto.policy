from Products.CMFCore.utils import getToolByName
from zope.publisher.browser import BrowserView
from zope.component.hooks import getSite

class CloneSiteView(BrowserView):
    """View pentru clonarea unui site Plone"""

    def __call__(self):
        source_site_id = self.request.get('site_sursa')
        target_site_id = self.request.get('target_site')
     import pdb;
        pdb.set_trace();
        # Obține obiectul aplicației
        app = self.context.getPhysicalRoot()
   
        # Verifică dacă site-ul sursă există
        source_site = app.get(source_site_id)
        if not source_site:
            self.request.response.setStatus(404)
            return f"Source site '{source_site_id}' not found."

        # Verifică dacă site-ul țintă există deja
        if target_site_id in app.objectIds():
            self.request.response.setStatus(400)
            return f"Target site '{target_site_id}' already exists."

        # Clonează site-ul
        app.manage_clone(source_site, target_site_id)

        # Reconstruiește catalogul pentru site-ul clonat
        target_site = app.get(target_site_id)
        catalog = getToolByName(target_site, 'portal_catalog')
        catalog.clearFindAndRebuild()

        self.request.response.setStatus(200)
        return f"Site '{source_site_id}' cloned successfully as '{target_site_id}'."

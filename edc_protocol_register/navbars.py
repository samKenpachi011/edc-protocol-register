from edc_navbar import NavbarItem, site_navbars, Navbar


edc_protocol_register = Navbar(name='protocols')

edc_protocol_register.append_item(
    NavbarItem(
        name='protocols',
        label='BHP Protocol Register',
        fa_icon='fa-user-plus',
        url_name='home_url'))

site_navbars.register(edc_protocol_register)

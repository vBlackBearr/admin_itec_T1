from reactpy import html

topbar = (
    html.nav(
        {"class": "navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow"},
        # Sidebar Toggle (Topbar)
        html.form(
            {"class": "form-inline"},
            html.button(
                {"id": "sidebarToggleTop", "class": "btn btn-link d-md-none rounded-circle mr-3"},
                html.i({"class": "fa fa-bars"})
            )
        ),
        # Topbar Search
        html.form(
            {"class": "d-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search"},
            html.div(
                {"class": "input-group"},
                html.input(
                    {"type": "text", "class": "form-control bg-light border-0 small",
                     "placeholder": "Search for...", "aria-label": "Search", "aria-describedby": "basic-addon2"}
                ),
                html.div(
                    {"class": "input-group-append"},
                    html.button(
                        {"class": "btn btn-primary", "type": "button"},
                        html.i({"class": "fas fa-search fa-sm"})
                    )
                )
            )
        ),
        # Topbar Navbar
        html.ul(
            {"class": "navbar-nav ml-auto"},
            # Nav Item - Search Dropdown (Visible Only XS)
            html.li(
                {"class": "nav-item dropdown no-arrow d-sm-none"},
                html.a(
                    {"class": "nav-link dropdown-toggle", "href": "#", "id": "searchDropdown", "role": "button",
                     "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                    html.i({"class": "fas fa-search fa-fw"})
                ),
                html.div(
                    {"class": "dropdown-menu dropdown-menu-right p-3 shadow animated--grow-in",
                     "aria-labelledby": "searchDropdown"},
                    html.form(
                        {"class": "form-inline mr-auto w-100 navbar-search"},
                        html.div(
                            {"class": "input-group"},
                            html.input(
                                {"type": "text", "class": "form-control bg-light border-0 small",
                                 "placeholder": "Search for...", "aria-label": "Search",
                                 "aria-describedby": "basic-addon2"}
                            ),
                            html.div(
                                {"class": "input-group-append"},
                                html.button(
                                    {"class": "btn btn-primary", "type": "button"},
                                    html.i({"class": "fas fa-search fa-sm"})
                                )
                            )
                        )
                    )
                )
            ),
            # Nav Item - Alerts
            html.li(
                {"class": "nav-item dropdown no-arrow mx-1"},
                html.a(
                    {"class": "nav-link dropdown-toggle", "href": "#", "id": "alertsDropdown", "role": "button",
                     "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                    html.i({"class": "fas fa-bell fa-fw"}),
                    html.span({"class": "badge badge-danger badge-counter"}, "3+")
                ),
                html.div(
                    {"class": "dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in",
                     "aria-labelledby": "alertsDropdown"},
                    html.h6({"class": "dropdown-header"}, "Alerts Center"),
                    html.a(
                        {"class": "dropdown-item d-flex align-items-center", "href": "#"},
                        html.div(
                            {"class": "mr-3"},
                            html.div(
                                {"class": "icon-circle bg-primary"},
                                html.i({"class": "fas fa-file-alt text-white"})
                            )
                        ),
                        html.div(
                            html.div(
                                {"class": "small text-gray-500"}, "December 12, 2019"
                            ),
                            html.span(
                                {"class": "font-weight-bold"}, "A new monthly report is ready to download!"
                            )
                        )
                    ),
                    # Otras alertas se pueden agregar de manera similar
                )
            ),
            # Nav Item - Messages
            html.li(
                {"class": "nav-item dropdown no-arrow mx-1"},
                html.a(
                    {"class": "nav-link dropdown-toggle", "href": "#", "id": "messagesDropdown", "role": "button",
                     "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                    html.i({"class": "fas fa-envelope fa-fw"}),
                    html.span({"class": "badge badge-danger badge-counter"}, "7")
                ),
                html.div(
                    {"class": "dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in",
                     "aria-labelledby": "messagesDropdown"},
                    html.h6({"class": "dropdown-header"}, "Message Center"),
                    # Mensajes se pueden agregar de manera similar
                )
            ),
            # Topbar Divider
            html.div({"class": "topbar-divider d-none d-sm-block"}),
            # Nav Item - User Information
            html.li(
                {"class": "nav-item dropdown no-arrow"},
                html.a(
                    {"class": "nav-link dropdown-toggle", "href": "#", "id": "userDropdown", "role": "button",
                     "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                    html.span({"class": "mr-2 d-none d-lg-inline text-gray-600 small"}, "Douglas McGee"),
                    html.img(
                        {"class": "img-profile rounded-circle", "src": "img/undraw_profile.svg"}
                    )
                ),
                html.div(
                    {"class": "dropdown-menu dropdown-menu-right shadow animated--grow-in",
                     "aria-labelledby": "userDropdown"},
                    html.a(
                        {"class": "dropdown-item", "href": "#"},
                        html.i({"class": "fas fa-user fa-sm fa-fw mr-2 text-gray-400"}),
                        "Profile"
                    ),
                    html.a(
                        {"class": "dropdown-item", "href": "#"},
                        html.i({"class": "fas fa-cogs fa-sm fa-fw mr-2 text-gray-400"}),
                        "Settings"
                    ),
                    html.a(
                        {"class": "dropdown-item", "href": "#"},
                        html.i({"class": "fas fa-list fa-sm fa-fw mr-2 text-gray-400"}),
                        "Activity Log"
                    ),
                    html.div({"class": "dropdown-divider"}),
                    html.a(
                        {"class": "dropdown-item", "href": "#", "data-toggle": "modal", "data-target": "#logoutModal"},
                        html.i({"class": "fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"}),
                        "Logout"
                    )
                )
            )
        )
    )
)

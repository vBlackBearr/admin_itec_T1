from reactpy import html, use_state
import reactpy
from localStoragePy import localStoragePy
from admin.content.api import Login

localStorage = localStoragePy('iTec_space', 'your-storage-backend')


def login():
    modal_content, set_modal_content = use_state("")
    modal_style, set_modal_style = use_state({"display": "none"})

    email, set_email = use_state("")
    password, set_password = use_state("")

    def show_modal():
        set_modal_style({"display": "block"})

    def hide_modal(e):
        set_modal_style({"display": "none"})

    modal_success = (
        html.div({

            "class": "modal-dialog modal-dialog-centered"
        },
            html.div({
                "class": "modal-content",
                "style": {
                    "align-content": "center",
                    "justify-content": "center",
                    "margin": "30px",
                    "padding": "30px",
                },
            },
                html.div({
                    "class": "modal-header"
                },
                    html.div(
                        html.h1({
                            "class": "modal-title fs-5",
                            "id": "exampleModalToggleLabel"
                        }, "Login Success!"),
                        html.a({
                            "href": "/admin/index",
                        },
                            html.button({
                                "class": "btn btn-primary"
                            },
                                "Go to Dashboard"
                            ),
                        ),
                    ),
                    # html.button({
                    #     "type": "button",
                    #     "class": "btn-close",
                    #     "data-bs-dismiss": "modal",
                    #     "aria-label": "Close",
                    #     "on_click": hide_modal
                    # }, "x")
                )
            )
        )
    )

    modal_fail = (
        html.div({

            "class": "modal-dialog modal-dialog-centered"
        },
            html.div({
                "class": "modal-content",
                "style": {
                    "align-content": "center",
                    "justify-content": "center",
                    "margin": "30px",
                    "padding": "30px",
                },
            },
                html.div({
                    "class": "modal-header"
                },
                    html.div(
                        html.h1({
                            "class": "modal-title fs-5",
                            "id": "exampleModalToggleLabel"
                        }, "Login failed"),
                        html.h5("Usuario y/o contraseña incorrecta!")
                        # html.a({
                        #     "href": "/admin/index",
                        # },
                        #     html.button({
                        #         "class": "btn btn-primary"
                        #     },
                        #         "Go to Dashboard"
                        #     ),
                        # ),
                    ),
                    html.button({
                        "type": "button",
                        "class": "btn-close",
                        "data-bs-dismiss": "modal",
                        "aria-label": "Close",
                        "on_click": hide_modal
                    }, "x")
                )
            )
        )
    )

    @reactpy.event(prevent_default=True)
    async def handleLogin(e):
        # print("handleLogin")
        response = await Login({"email": email, "password": password})
        if response["status"] == 200:
            set_modal_content(modal_success)
            # set_modal_content("Hola")
            show_modal()
            print("Inicio de sesion exitoso")
            localStorage.setItem('token', response["data"]["token"])
        else:
            if response["status"] == 401:
                # set_modal_content("Usuario y/o contraseña incorrecta!")
                set_modal_content(modal_fail)
                show_modal()
                print("Usuario y/o contraseña incorrecta!")
            else:
                print("Ocurrio un error desconocido al iniciar sesion")
                # set_modal_content("Error al iniciar sesion")
        # show_modal(None)

    # @reactpy.event(prevent_default=True)
    # async def handleLogin(e):
    #     response = await Login({"email": email, "password": password})
    #     if response["status"] == 200:
    #         set_modal_content("Login Success!")
    #         localStorage.setItem('token', response["data"]["token"])
    #     else:
    #         if response["status"] == 401:
    #             set_modal_content("Usuario y/o contraseña incorrecta!")
    #         else:
    #             set_modal_content("Error al iniciar sesion")
    #     show_modal(None)

    return (
        #
        #    MODAL
        #
        html.div({
            "style": modal_style,
            "class": "modal"
        },
            modal_content
        ),
        #
        #   Fin MODAL
        #

        html.div({"class": "container"},
                 html.div({"class": "row justify-content-center"},
                          html.div({"class": "col-xl-10 col-lg-12 col-md-9"},
                                   html.div({"class": "card o-hidden border-0 shadow-lg my-5"},
                                            html.div({"class": "card-body p-0"},
                                                     html.div({"class": "row"},
                                                              html.div({
                                                                  "class": "col-lg-6 d-none d-lg-block bg-login-image"}, ),
                                                              html.div({"class": "col-lg-6"},
                                                                       html.div({"class": "p-5"},
                                                                                html.div(
                                                                                    {"class": "text-center"},
                                                                                    html.h1({
                                                                                        "class": "h4 text-gray-900 mb-4"},
                                                                                        "Welcome Back!"),
                                                                                ),
                                                                                html.form({"class": "user"},
                                                                                          html.div({
                                                                                              "class": "form-group"},
                                                                                              html.input({
                                                                                                  "type": "email",
                                                                                                  "class": "form-control form-control-user",
                                                                                                  "id": "exampleInputEmail",
                                                                                                  "aria-describedby": "emailHelp",
                                                                                                  "placeholder": "Enter Email Address...",
                                                                                                  "on_change": lambda
                                                                                                      e: set_email(
                                                                                                      e["target"][
                                                                                                          "value"]),
                                                                                              })
                                                                                          ),
                                                                                          html.div({
                                                                                              "class": "from-group"},
                                                                                              html.input({
                                                                                                  "type": "password",
                                                                                                  "class": "form-control form-control-user",
                                                                                                  "id": "exampleInputPassword",
                                                                                                  "placeholder": "Password",
                                                                                                  "on_change": lambda
                                                                                                      e: set_password(
                                                                                                      e["target"][
                                                                                                          "value"]),
                                                                                              })
                                                                                          ),
                                                                                          html.div({
                                                                                              "class": "form-group"},
                                                                                              html.div({
                                                                                                  "class": "custom-control custom-checkbox small"},
                                                                                                  html.input(
                                                                                                      {
                                                                                                          "type": "checkbox",
                                                                                                          "class": "custom-control-input",
                                                                                                          "id": "customCheck"}),
                                                                                                  html.label(
                                                                                                      {
                                                                                                          "class": "custom-control-label",
                                                                                                          "for": "customCheck"},
                                                                                                      "Remember Me")
                                                                                              ),
                                                                                          ),
                                                                                          html.a({
                                                                                              # "href": "index.html",
                                                                                              "class": "btn btn-primary btn-user btn-block",
                                                                                              "on_click": handleLogin},
                                                                                              "Login"),
                                                                                          html.hr(),
                                                                                          # html.a({
                                                                                          #     "href": "index.html",
                                                                                          #     "class": "btn btn-google btn-user btn-block"},
                                                                                          #     html.i({
                                                                                          #         "class": "fab fa-google fa-fw"}),
                                                                                          #     "Login with Google"
                                                                                          # ),
                                                                                          # html.a({
                                                                                          #     "href": "index.html",
                                                                                          #     "class": "btn btn-facebook btn-user btn-block"},
                                                                                          #     html.i({
                                                                                          #         "class": "fab fa-facebook-f fa-fw"}),
                                                                                          #     "Login with Facebook"
                                                                                          # )
                                                                                          ),
                                                                                html.hr(),
                                                                                html.div(
                                                                                    {"class": "text-center"},
                                                                                    html.a({"class": "small",
                                                                                            "href": "#"},
                                                                                           "Forgot Password?")
                                                                                ),
                                                                                # html.div(
                                                                                #     {"class": "text-center"},
                                                                                #     html.a({"class": "small",
                                                                                #             "href": "#"},
                                                                                #            "Create an Account!")
                                                                                # )
                                                                                )
                                                                       )
                                                              )
                                                     )
                                            )
                                   )
                          )
                 )
    )

from reactpy import html

head = (
    html.link({
        "href": "/admin/content/css/sb-admin-2.min.css",
        "rel": "stylesheet"
    }),
    html.link({
        "href": "/admin/content/css/all.min.css",
        "rel": "stylesheet",
        "type": "text/css"
    }),
    html.script(
        {"src": "/admin/content/js/jquery.min.js"}),
    html.script(
        {"src": "/admin/content/js/bootstrap.bundle.min.js"}),
    html.script(
        {"src": "/admin/content/js/jquery.easing.min.js"}),
    html.script(
        {"src": "/admin/content/js/sb-admin-2.min.js"}),
    html.script(
        {"src": "/admin/content/js/Chart.min.js"}),
    html.script(
        {"src": "/admin/content/js/chart-area-demo.js"}),
    html.script(
        {"src": "/admin/content/js/chart-pie-demo.js"}),
    html.meta({
        "charset": "utf-8"
    }),
    html.meta({
        "http-equiv": "X-UA-Compatible",
        "content": "IE=edge"
    }),
    html.meta({
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
    }),
    html.meta({
        "name": "description",
        "content": ""
    }),
    html.meta({
        "name": "author",
        "content": ""
    }),
    html.title("PANEL ADMINISTRADOR"),
    html.link({
        "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
        "rel": "stylesheet",
        "type": "text/css"
    }),
    html.link({
        "href": "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,"
                "800,800i,900,900i",
        "rel": "stylesheet"
    })
)

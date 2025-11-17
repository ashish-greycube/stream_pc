app_name = "stream_pc"
app_title = "Stream PC"
app_publisher = "GreyCube Technologies"
app_description = "Customization of stream app for pure clean"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/stream_pc/css/stream_pc.css"
# app_include_js = "/assets/stream_pc/js/stream_pc.js"

# include js, css files in header of web template
# web_include_css = "/assets/stream_pc/css/stream_pc.css"
# web_include_js = "/assets/stream_pc/js/stream_pc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "stream_pc/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "stream_pc.utils.jinja_methods",
# 	"filters": "stream_pc.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "stream_pc.install.before_install"
# after_install = "stream_pc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "stream_pc.uninstall.before_uninstall"
# after_uninstall = "stream_pc.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "stream_pc.utils.before_app_install"
# after_app_install = "stream_pc.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "stream_pc.utils.before_app_uninstall"
# after_app_uninstall = "stream_pc.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "stream_pc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Event Producer GC": {
		"on_change": "stream_pc.api.payment_type_allow_on_submit",
	},
    "Delivery Note": {
        "on_update_after_submit": "stream_pc.api.update_payment_type_in_so",
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"stream_pc.tasks.all"
# 	],
# 	"daily": [
# 		"stream_pc.tasks.daily"
# 	],
# 	"hourly": [
# 		"stream_pc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"stream_pc.tasks.weekly"
# 	],
# 	"monthly": [
# 		"stream_pc.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "stream_pc.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "stream_pc.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "stream_pc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["stream_pc.utils.before_request"]
# after_request = ["stream_pc.utils.after_request"]

# Job Events
# ----------
# before_job = ["stream_pc.utils.before_job"]
# after_job = ["stream_pc.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"stream_pc.auth.validate"
# ]

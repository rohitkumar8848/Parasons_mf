from . import __version__ as app_version

app_name = "parasons_mf"
app_title = "Parasons MF"
app_publisher = "8848"
app_description = "manufacturing customization for Parasons"
app_email = "rohitkumar@8848digital.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/parasons_mf/css/parasons_mf.css"
# app_include_js = "/assets/parasons_mf/js/parasons_mf.js"

# include js, css files in header of web template
# web_include_css = "/assets/parasons_mf/css/parasons_mf.css"
# web_include_js = "/assets/parasons_mf/js/parasons_mf.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "parasons_mf/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Work Order" : "customizations/work_order/work_order.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------
# Class Function Overrides
from erpnext.manufacturing.doctype.work_order.work_order import WorkOrder
from parasons_mf.customizations.work_order.work_order import set_required_items

WorkOrder.set_required_items = set_required_items
# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "parasons_mf.utils.jinja_methods",
#	"filters": "parasons_mf.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "parasons_mf.install.before_install"
# after_install = "parasons_mf.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "parasons_mf.uninstall.before_uninstall"
# after_uninstall = "parasons_mf.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "parasons_mf.utils.before_app_install"
# after_app_install = "parasons_mf.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "parasons_mf.utils.before_app_uninstall"
# after_app_uninstall = "parasons_mf.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "parasons_mf.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"parasons_mf.tasks.all"
#	],
#	"daily": [
#		"parasons_mf.tasks.daily"
#	],
#	"hourly": [
#		"parasons_mf.tasks.hourly"
#	],
#	"weekly": [
#		"parasons_mf.tasks.weekly"
#	],
#	"monthly": [
#		"parasons_mf.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "parasons_mf.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "parasons_mf.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "parasons_mf.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["parasons_mf.utils.before_request"]
# after_request = ["parasons_mf.utils.after_request"]

# Job Events
# ----------
# before_job = ["parasons_mf.utils.before_job"]
# after_job = ["parasons_mf.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"parasons_mf.auth.validate"
# ]
fixtures = [
    {"dt": "Custom Field", "filters": [["module", "=", "Parasons MF"]]},
]

app_name = "project_hub"
app_title = "Project Hub"
app_publisher = "Nigma Tech Limited"
app_description = "ERPNext Customizations for Project and Events"
app_email = "tripleo4u@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "project_hub",
# 		"logo": "/assets/project_hub/logo.png",
# 		"title": "Project Hub",
# 		"route": "/project_hub",
# 		"has_permission": "project_hub.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/project_hub/css/project_hub.css"
# app_include_js = "/assets/project_hub/js/project_hub.js"

# include js, css files in header of web template
# web_include_css = "/assets/project_hub/css/project_hub.css"
# web_include_js = "/assets/project_hub/js/project_hub.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "project_hub/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "project_hub/public/icons.svg"

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
# 	"methods": "project_hub.utils.jinja_methods",
# 	"filters": "project_hub.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "project_hub.install.before_install"
after_install = "project_hub.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "project_hub.uninstall.before_uninstall"
# after_uninstall = "project_hub.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "project_hub.utils.before_app_install"
# after_app_install = "project_hub.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "project_hub.utils.before_app_uninstall"
# after_app_uninstall = "project_hub.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "project_hub.notifications.get_notification_config"

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
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
    "Project" : {
        "validate" : "project_hub.overrides.check_has_value_changed"
    },
    "Meeting" : {
		"on_submit" : "project_hub.overrides.update_meetings"
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    "cron" : {
		"0 9 * * *" : [
			"project_hub.overrides.send_email_by_9am" 

		],
		"0 0 1 */3 *" : [
			"project_hub.overrides.send_opportunity_reminder" 
		]
		
	}
	# "all": [
	# 	"project_hub.tasks.all"
	# ],
	# "daily": [
	# 	"project_hub.tasks.daily"
	# ],
	# "hourly": [
	# 	"project_hub.tasks.hourly"
	# ],
	# "weekly": [
	# 	"project_hub.tasks.weekly"
	# ],
	# "monthly": [
	# 	"project_hub.tasks.monthly"
	# ],
}

# Testing
# -------

# before_tests = "project_hub.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "project_hub.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "project_hub.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["project_hub.utils.before_request"]
# after_request = ["project_hub.utils.after_request"]

# Job Events
# ----------
# before_job = ["project_hub.utils.before_job"]
# after_job = ["project_hub.utils.after_job"]

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
# 	"project_hub.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "fa_depreciation"
app_title = "Fixed Asset Depreciation"
app_publisher = "Akshay Mehta"
app_description = "Provides Report for Depreciation on Fixed Assets"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mehta.akshay@gmail.com"
app_version = "0.0.1"
app_license = "MIT"
fixtures = ["Custom Field"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fa_depreciation/css/fa_depreciation.css"
# app_include_js = "/assets/fa_depreciation/js/fa_depreciation.js"

# include js, css files in header of web template
# web_include_css = "/assets/fa_depreciation/css/fa_depreciation.css"
# web_include_js = "/assets/fa_depreciation/js/fa_depreciation.js"

# Home Pages
# ----------

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

# Installation
# ------------

# before_install = "fa_depreciation.install.before_install"
# after_install = "fa_depreciation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fa_depreciation.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"fa_depreciation.tasks.all"
# 	],
# 	"daily": [
# 		"fa_depreciation.tasks.daily"
# 	],
# 	"hourly": [
# 		"fa_depreciation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"fa_depreciation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"fa_depreciation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "fa_depreciation.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "fa_depreciation.event.get_events"
# }


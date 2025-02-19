import frappe
from erpnext.projects.doctype.project.project import Project
from erpnext.setup.doctype.holiday_list.holiday_list import is_holiday
from frappe.utils import add_days, flt, get_datetime, get_time, get_url, nowtime, today
from frappe import _


def check_has_value_changed(doc,event):
	#check if value has changed
	fields = ["status", "project_type", "is_active", "priority", 
		"expected_start_date", "expected_end_date","project_name", "notes", "users"]
	for field in fields:
		if doc.has_value_changed(field):
			#send email notifcation
			if field ==  "users":
				if [i.email for i in doc.users if not i.welcome_email_sent]:
					recipients = [i.email for i in doc.users if doc.users]
					if recipients:
						send_email_notification(field,doc.name,recipients)
			else:
				recipients = [i.email for i in doc.users if doc.users]
				if recipients:
					send_email_notification(field,doc.name,recipients)
			pass
		
def send_email_notification(field,project_name,recipients):
	
	'''Send email for value changed '''
	link_to_project = frappe.utils.get_url_to_form("Project",project_name)
	message = f"Value changed for field <b>{field}</b> in project {project_name} <br>" + "please log in and check <br>" + f"<a href={link_to_project}> project </a>"
	recipients = recipients
	subject = f"Value Changed in Project {project_name}"
	frappe.sendmail(recipients=recipients,
					subject=subject,message=message,now=True)
	frappe.db.commit()
	

def send_project_reminder():
	'''Send Project reminder on custom days'''
	#send daily project reminder first
	# send the reminders set to custom days
	projects = frappe.get_all("Project",{"collect_progress":1,"status":"Open"},
							  ["name","holiday_list","custom_monday","custom_tuesday","custom_wednesday",
							   "custom_thursday","custom_friday","custom_email_message"])
	for project in projects:
		if not is_holiday(project["holiday_list"]) :
			#send daily email reminders
			send_project_update_email_to_users(project)
			#send emails for custom days wednesday and friday ie 3 and 5
			if project["custom_monday"] and get_datetime().isoweekday() == 1:
				send_custom_email(project)
			if project["custom_tuesday"] and get_datetime().isoweekday() == 2:
				send_custom_email(project)
			if project["custom_wednesday"] and get_datetime().isoweekday() == 3:
				send_custom_email(project)
			if project["custom_thursday"] and get_datetime().isoweekday() == 4:
				send_custom_email(project)
			if project["custom_friday"] and get_datetime().isoweekday() == 5:
				send_custom_email(project)
										


def send_custom_email(project):
	doc = frappe.get_doc("Project", project["name"])

	if is_holiday(doc.holiday_list) or not doc.users:
		return

	message = f"Please send update on project {project['name']}"
	subject = "For project %s, update your status" % (project['name'])

	incoming_email_account = frappe.db.get_value(
		"Email Account", dict(enable_incoming=1, default_incoming=1), "email_id"
	)

	frappe.sendmail(
		recipients=get_users_email(doc),
		message=message,
		subject=_(subject),
		now=True,
		reply_to=incoming_email_account,
	)


	
def send_project_update_email_to_users(project):
	doc = frappe.get_doc("Project", project["name"])

	if is_holiday(doc.holiday_list) or not doc.users:
		return

	timesheet = frappe.utils.get_url_to_list("Timesheet") + "/new-timesheet-inwadpbyui"
	timesheet = f"<a href = {timesheet}> <b> New Timesheet</b>"
	project_update = frappe.utils.get_url_to_list("Project Update") + "/new-project-update-xijvwoacbb"
	project_update = f"<a href = {project_update}> <b> New Project Update</b>"
	
	message = frappe.render_template(project["custom_email_message"],{"timesheet":timesheet,"project_update":project_update})

	subject = "Daily project email %s, update your status" % (project["name"])

	incoming_email_account = frappe.db.get_value(
		"Email Account", dict(enable_incoming=1, default_incoming=1), "email_id"
	)
	project_update = frappe.get_doc(
		{
			"doctype": "Project Update",
			"project": project,
			"sent": 0,
			"date": today(),
			"time": nowtime(),
			"naming_series": "UPDATE-.project.-.YY.MM.DD.-",
		}
	).insert()

	frappe.sendmail(
		recipients=get_users_email(doc),
		message=message,
		subject=_(subject),
		reference_doctype=project_update.doctype,
		reference_name=project_update.name,
		reply_to=incoming_email_account,
	)


def get_users_email(doc):
	return [d.email for d in doc.users if frappe.db.get_value("User", d.user, "enabled")]

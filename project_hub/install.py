import frappe

def after_install():
    add_options_to_project()

def add_options_to_project():
    project =  frappe.get_meta("Project").get_field("frequency")
    
    
    project_options = project.options.split("\n")
    project_options.append("Custom")
   
    project_options = "\n".join(project_options)
    
    project.options = project_options
    project.save()
    frappe.db.commit()
    
    
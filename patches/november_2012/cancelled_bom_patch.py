import webnotes

def execute():
	cancelled_boms = webnotes.conn.sql("""select name from `tabBOM`
		where docstatus = 2""")
	
	for bom in cancelled_boms:
		webnotes.conn.sql("""update `tabBOM` set is_default=0, is_active='No'
			where name=%s""", (bom[0],))
		
		webnotes.conn.sql("""update `tabItem` set default_bom=null
			where default_bom=%s""", (bom[0],))
		
		
import streamlit as st
import yaml
import mysql.connector as mysql
from db_connection import get_database_connection
from sqlalchemy import create_engine
from uuid import uuid1
PAGE_CONFIG = {"page_title":"Admission-Portal","page_icon":"🎓","layout":"centered","initial_sidebar_state":"auto"}
st.set_page_config(**PAGE_CONFIG)
st.title("Diploma in Data Science Admission Portal")
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background: url("https://images.unsplash.com/photo-1547190027-9156686aa2f0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80")
    }
    </style>
    """,
    unsafe_allow_html=True)
# def main():
	
# 	if op == "Admin":
# 		admin()



# def get_database_connection():
#     db = mysql.connect(host = "127.0.0.1",
#                       user = "root",
#                       passwd = "sharia",
#                       database = "infoDB",
#                       auth_plugin='mysql_native_password')
#     cursor = db.cursor()
#     # cursor.execute("Show database")
#     print(database)
#     return cursor, db

cursor,db = get_database_connection()


# cursor.execute("Select * from studentinfo")
# databases = cursor.fetchall() ## it returns a list of all databases present
# st.write(databases)

# cursor.execute('''CREATE TABLE studentinfo (id varchar(20) PRIMARY KEY,
#                                       student_name varchar(255),
#                                       fathers_name varchar(255),
#                                       mothers_name varchar(255),
#                                       present_address varchar(500),
#                                       permanent_address varchar(500),
#                                       contact_no varchar(11),
#                                       email varchar(255),
#                                       gpa varchar(10),
#                                       religion varchar(255),
#                                       nationality varchar(15),
#                                       reg_date date,
#                                       date_of_birth date,
#                                       gender varchar(8))''')

# tables = cursor.fetchall()
# st.write(tables)

			###Searching the data from selected rage

# def searchdata(start_date,end_date):
	


def admin():
	# https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1170&q=80
	
	st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1547190027-9156686aa2f0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80")
    }
    </style>
    """,
    unsafe_allow_html=True)
	username = st.sidebar.text_input('Username', 'Enter Your E-mail', key='user')
	password = st.sidebar.text_input("Enter a password", type="password", key='pass')
	st.session_state.login = st.sidebar.checkbox('Log In')
	if st.session_state.login:
	 	if username.split('@')[-1] == "gmail.com" and password == "sharia":
	 		st.subheader("Logged as Admin")
	 		col1,col2,col3= st.columns((2,0.1,2))
	 		start_date=col1.date_input('From')
	 		col2.write(" ")
	 		col2.write(" ")
	 		col2.write(" ")
	 		col2.write("-")
	 		end_date=col3.date_input('To')
	 		radiobutt=col1.radio('',('Accpeted','Rejected','In Progress'))
	 		if radiobutt=='Rejected':
	 			s = 'Rejected'
	 		elif radiobutt=='Accpeted':
	 			s = 'Accpeted'
	 		else:
	 			s = 'In Progress'
	 		query = f'''Select * from studentinfo where reg_date between '{start_date}'and'{end_date}' and status='{s}' '''
	 		cursor.execute(query)
	 		tables = cursor.fetchall()
	 		j=1
	 		for m in tables:
	 			with st.container():
		 			col4,col5 = st.columns((2,2))
		 			col4.subheader(f'Student Details --->')
	 				
	 				col5.subheader(f"{j} ")
	 				j=j+1
		 			col4.write(f"Name                ")
		 			col5.write(m[1])
		 			col4.write(f'''Father's Name    ''')
		 			col5.write(m[2])
		 			col4.write(f'''Mother's Name    ''')
		 			col5.write(m[3])
		 			col4.write(f'''Present Address    ''')
		 			col5.write(m[4])
		 			col4.write(f'''Permanent Address    ''')
		 			col5.write(m[5])
		 			col4.write(f'''Contact    ''')
		 			col5.write(m[6])
		 			col4.write(f'''Email     ''')
		 			col5.write(m[7])
		 			col4.write(f'''GPA    ''')
		 			col5.write(m[8])
		 			col4.write(f'''Religion    ''')
		 			col5.write(m[9])
		 			col4.write(f'''Nationality    ''')
		 			col5.write(m[10])
		 			col4.write(f'''Regestration Date    ''')
		 			col5.write(f'{m[11]}')
		 			col4.write(f'''Birth Date    ''')
		 			col5.write(f'm[12]')
		 			col4.write(f'''Gender''')
		 			col5.write(m[13])
		 			if s=='In Progress':
		 				with st.container():
		 					col7,col8 = st.columns((0.3,2))
			 				ac_button=col7.button("Accept",key=m[0])
			 				reject_button=col7.button("Reject",key=m[0])
				 			str = "Accpeted"
				 			if ac_button:
				 				col8.success("Accpeted")
				 				update_query = f'''Update studentinfo set status='Accpeted' where id = '{m[0]}' '''
				 				cursor.execute(update_query)
				 				db.commit()
				 				database = cursor.fetchall()
				 				st.balloons()
				 			if reject_button:
				 				col8.error("Rejected")
				 				update_query = f'''Update studentinfo set status='Rejected' where id = '{m[0]}' '''
				 				cursor.execute(update_query)
				 				db.commit()

	 	else:
	 		st.sidebar.warning('Wrong Credintials')


def show_details():
	with st.form(key='show_details'):
		st.subheader("Student Information")
		st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1585314062340-f1a5a7c9328d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=387&q=80")
    }
    </style>
    """,
    unsafe_allow_html=True)
		search_id = st.text_input("Enter Your ID")
		if(st.form_submit_button('Search')):
				query = f'''select id,student_name,fathers_name,mothers_name,present_address,permanent_address,contact_no,email,gpa, 
			                                            religion,nationality,reg_date,date_of_birth,gender from studentinfo'''
				cursor.execute(query)
				database = cursor.fetchall()
				member_found_flag = False
				col1,col3,col2 = st.columns((2,1,4))
				for m in database:
					if search_id == m[0]:
						st.success('These are the information of yours we find!')
						col1.write(f"Name                ")
						col3.write(":")
						col2.write(m[1])
						col1.write(f'''Father's Name    ''')
						col3.write(":")
						col2.write(m[2])
						col1.write(f'''Mother's Name    ''')
						col3.write(":")
						col2.write(m[3])
						col1.write(f'''Present Address    ''')
						col3.write(":")
						col2.write(m[4])
						col1.write(f'''Permanent Address    ''')
						col3.write(":")
						col2.write(m[5])
						col1.write(f'''Contact    ''')
						col3.write(":")
						col2.write(m[6])
						col1.write(f'''Email     ''')
						col3.write(":")
						col2.write(m[7])
						col1.write(f'''GPA    ''')
						col3.write(":")
						col2.write(m[8])
						col1.write(f'''Religion    ''')
						col3.write(":")
						col2.write(m[9])
						col1.write(f'''Nationality    ''')
						col3.write(":")
						col2.write(m[10])
						col1.write(f'''Regestration Date    ''')
						col3.write(":")
						col2.write(m[11])
						col1.write(f'''Birth Date    ''')
						col3.write(":")
						col2.write(m[12])
						col1.write(f'''Gender''')
						col3.write(":")
						col2.write(m[13])
						member_found_flag = True
						break
				if member_found_flag == False:
						st.warning('Sorry, not available.')	

def student_reg():
	st.subheader("Student Regestration")
	st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1625535069703-a67ae00bd6de?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1332&q=80")
    }
    </style>
    """,
    unsafe_allow_html=True)
	with st.form(key='student_reg'):
		
		student_name = st.text_input("Name")
		fathers_name = st.text_input("Father's Name")
		mothers_name = st.text_input("Mother's Name")
		present_address = st.text_area("Present Address")
		permanent_address = st.text_area("Permanent Address")
		email = st.text_input("E-mail")
		mobile = st.text_input('Mobile')
		gpa = st.text_input("GPA")
		religion = st.selectbox("Religion",('--Select Religion--','Islam','Hindu','Cristian'))
		nationality = st.text_input("Nationality")
		reg_date = st.date_input("Registration Date")
		date_of_birth = st.date_input("Bith Date")
		gender = st.radio('Gender', ('Male', 'Female'))
		submitted=0
		if st.form_submit_button('Submit'):
			x = uuid1()
			x = str(x)[:20]
			col1,col2 = st.columns((4,3))
			col1.warning("Please Store your ID!!")
			col1.info("Your ID is : ")
			col1.code(x)

			query = f'''INSERT INTO studentinfo (id ,student_name,fathers_name,mothers_name,present_address,permanent_address,contact_no,email,gpa, 
                                            religion,nationality,reg_date,date_of_birth,gender) 
                                    VALUES ( '{x}', '{student_name}', '{fathers_name}', '{mothers_name}', '{present_address}', '{permanent_address}','{mobile}', '{email}', '{gpa}', '{religion}', '{nationality}' ,'{reg_date}' ,'{date_of_birth}', '{gender}')'''
			cursor.execute(query)
			db.commit()
			st.success(f'{student_name} info inserted successfully')
			st.balloons()
					

def check_stat():
	st.subheader("Status Check...")
	st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1585314062340-f1a5a7c9328d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=387&q=80")
    }
    </style>
    """,
    unsafe_allow_html=True)
	search_id = st.text_input('Give your id')
	search_button = st.button('Search')
	if search_button:
		query = f'''Select status from studentinfo where id='{search_id}' '''
		cursor.execute(query)
		# db.commit()
		database = cursor.fetchall()
		f=False
		for i in database:
			if i[0]=='In Progress':
				f=True
				st.info(f"Your request is '{i[0]}'")
			elif i[0]=='Accpeted':
				f=True
				st.success(f"Your request is '{i[0]}'")
			elif i[0]=='Rejected':
				f=True
				st.error(f"Your request is '{i[0]}'")
		if f==False:
			st.warning("Wrong Input")

def forget_pass():
	st.subheader(" ")
	st.subheader(" ")
	st.subheader(" ")
	st.text_input("Give your E-mail")
	st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1553451166-232112bda6f6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1172&q=80")
    }
    </style>
    """,
    unsafe_allow_html=True)

def main():
	op = st.sidebar.selectbox('',('--Select One--','Admin','Student Registration','Show Student Details','Check status','Forget Code'))
	st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1559311648-874c28a0b7c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1147&q=80")
    }
    </style>
    """,
    unsafe_allow_html=True)
	if op=="Admin":
		admin()
	if op=="Student Registration":
		student_reg()
	if op=='Show Student Details':
		show_details()
	if op=='Check status':
		check_stat()
	if op=='Forget Code':
		forget_pass()


	    
if __name__ == '__main__':
	main()

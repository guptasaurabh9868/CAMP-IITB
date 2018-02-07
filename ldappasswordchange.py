from subprocess import call


# call(["ping", "127.0.0.1"])
call(["/usr/bin/ldappasswd " " -H " " ldap://10.100.115.208 " " -x " " -D " " \"cn=Digvijaysingh Gour,cn=people,dc=iitb,dc=ac,dc=in\" " " -W " " -A " " -S "])
#OpenVPN Client key OVPN generator
#Borrowed liberally from DigitalOcean's OpenVPN initialization script
#Need to add command line arg ability
#Need to fix the source ./vars issue at the onset

import subprocess
#subprocess.call(["command1", "arg1", "arg2"])

#define names of keys
keynames = ("henry","jimbo")
#set IP address of VPN server
ipaddr = "127.0.0.1" 

for thiskey in keynames:
        #Update vars config -- NOT WORKING right now - Have manually run source ./vars in that sub folder before running this
        subprocess.call("cd /etc/openvpn/easy-rsa && source ./vars",shell=True)
        #Build the keys
        subprocess.call("cd /etc/openvpn/easy-rsa && ./build-key --batch "+thiskey,shell=True)
        #Time to build the OVPN file
        arg2 = "/etc/openvpn/easy-rsa/keys/" + thiskey + ".ovpn"
        #print "ARG2:",arg2
        subprocess.call(['cp /usr/share/doc/openvpn/examples/sample-config-files/client.conf '+arg2],shell=True)
        arg3 = "\'s/my-server-1/" + ipaddr + "/\'"
        subprocess.call('sed -ie '+arg3+' '+arg2,shell=True)
        subprocess.call("sed -ie \'s/;user nobody/user nobody/\' "+arg2,shell=True)
        subprocess.call("sed -ie \'s/;group nogroup/group nogroup/\' "+arg2,shell=True)
        subprocess.call("sed -ie \'s/ca ca.crt//\' "+arg2,shell=True)
        subprocess.call("sed -ie \'s/cert client.crt//\' "+arg2,shell=True)
        subprocess.call("sed -ie \'s/key client.key//\' "+arg2,shell=True)
        subprocess.call('echo "<ca>" >> '+arg2,shell=True)
        subprocess.call("cat /etc/openvpn/ca.crt >> "+arg2,shell=True)
        subprocess.call('echo "</ca>" >> '+arg2,shell=True)
        subprocess.call('echo "<cert>" >> '+arg2,shell=True)
        arg4 = "/etc/openvpn/easy-rsa/keys/" + thiskey + ".crt"
        subprocess.call("openssl x509 -outform PEM -in "+arg4+" >> "+arg2,shell=True)
        subprocess.call('echo "</cert>" >> '+arg2,shell=True)
        subprocess.call('echo "<key>" >> '+arg2,shell=True)
        arg5 = "/etc/openvpn/easy-rsa/keys/" + thiskey + ".key"
        subprocess.call('cat "'+arg5+'" >> '+arg2,shell=True)
        subprocess.call('echo "</key>" >>'+arg2,shell=True)
        print (thiskey+': key successfully generated. ('+arg2+')')

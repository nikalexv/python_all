# cat /usr/share/doc/dhcp*/dhcpd.conf.sample
# dhcpd.conf
#
# Sample configuration file for ISC dhcpd
#

# option definitions common to all supported networks...
#option domain-name "example.org";
#option domain-name-servers ns1.example.org, ns2.example.org;
#a < b
#[a;b]
n = int(input())
s = 0
for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact *= j
    s += fact 
print(s)

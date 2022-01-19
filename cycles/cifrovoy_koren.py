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
while n > 9:
    s = 0
    while n > 0:
        dig = n % 10
        s += dig
        n //=  10
    n = s    
print(n)


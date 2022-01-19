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
a, b = int(input()), int(input())
for i in range(a,b+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)

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
s = 0
s_max = 0
for i in range(a,b+1):
    for j in range(1,i+1):
        if i % j == 0:
            s += j
    if s >= s_max:
        s_max = s
        k = i
    s = 0
print(k, s_max)


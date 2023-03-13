DNS="18.202.130.238"
DOMAIN="flag.be"

dig ANY @$DNS_IP $DOMAIN     #Any information
dig A @$DNS_IP $DOMAIN       #Regular DNS request
dig AAAA @$DNS_IP $DOMAIN    #IPv6 DNS request
dig TXT @$DNS_IP $DOMAIN     #Information
dig MX @$DNS_IP $DOMAIN      #Emails related
dig NS @$DNS_IP $DOMAIN      #DNS that resolves that name

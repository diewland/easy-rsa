rm -rf pki/
./easyrsa init-pki
./easyrsa build-ca nopass
./easyrsa build-server-full localhost nopass

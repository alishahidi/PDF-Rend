checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then
   printf "\e[1;77mPlease, run this program as root!\n\e[0m"
   exit 1
fi

}

checkroot
apt-get update
apt-get install python -y
apt-get install python3 -y
apt-get install python3-pip -y
pip install --upgrade pip
python3 -m pip install -r requirments.txt
echo "Installed!"

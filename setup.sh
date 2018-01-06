echo "Installing dependencies into your environment"
pip install -r requirements.txt
clear

echo "Type in your telegram key"
read comchatter

echo "\n"
echo "Great work!\n"
export comchatter=$comchatter
echo "Exported comchatter environment variable.\n"

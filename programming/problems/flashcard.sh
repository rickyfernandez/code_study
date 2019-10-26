file=$(find . -type f -name '*.py' | sort -R | tail -1)
echo ""
echo "Time to restudy:"
echo "Random file chose: ${file}"
echo ""
read -n1 -r -p "Press space to continue..."
vim $file

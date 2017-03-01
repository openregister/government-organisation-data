#!/bin/sh

# <label for="buyer_id_220512" class=" selected" >Bedford Borough Council</label>

echo "buyer-id	name"
grep ' for="buyer_id_' | sed -e 's/^.*buyer_id_//' -e 's/<\/label>.*$//' -e 's/" *class.*>/	/'

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd1c6556",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "1. Add Contact\n",
      "2. Delete Contact\n",
      "3. Search Contact\n",
      "4. List Contacts\n",
      "5. Exit\n"
     ]
    }
   ],
   "source": [
    "contacts = {}\n",
    "\n",
    "def add_contact(name, number):\n",
    "    contacts[name] = number\n",
    "    print(f\"Added {name} with number {number} to contacts.\")\n",
    "\n",
    "def delete_contact(name):\n",
    "    if name in contacts:\n",
    "        del contacts[name]\n",
    "        print(f\"Deleted {name} from contacts.\")\n",
    "    else:\n",
    "        print(f\"{name} not found in contacts.\")\n",
    "\n",
    "def search_contact(name):\n",
    "    if name in contacts:\n",
    "        print(f\"Name: {name}, Number: {contacts[name]}\")\n",
    "    else:\n",
    "        print(f\"{name} not found in contacts.\")\n",
    "\n",
    "def list_contacts():\n",
    "    if contacts:\n",
    "        print(\"Contacts:\")\n",
    "        for name, number in contacts.items():\n",
    "            print(f\"Name: {name}, Number: {number}\")\n",
    "    else:\n",
    "        print(\"No contacts found.\")\n",
    "\n",
    "while True:\n",
    "    print(\"\\n1. Add Contact\")\n",
    "    print(\"2. Delete Contact\")\n",
    "    print(\"3. Search Contact\")\n",
    "    print(\"4. List Contacts\")\n",
    "    print(\"5. Exit\")\n",
    "    choice = input(\"Enter your choice (1-5): \")\n",
    "\n",
    "    if choice == '1':\n",
    "        name = input(\"Enter name: \")\n",
    "        number = input(\"Enter number: \")\n",
    "        add_contact(name, number)\n",
    "    elif choice == '2':\n",
    "        name = input(\"Enter name to delete: \")\n",
    "        delete_contact(name)\n",
    "    elif choice == '3':\n",
    "        name = input(\"Enter name to search: \")\n",
    "        search_contact(name)\n",
    "    elif choice == '4':\n",
    "        list_contacts()\n",
    "    elif choice == '5':\n",
    "        break\n",
    "    else:\n",
    "        print(\"Invalid choice. Please try again.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7266857e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

from pprint import pprint
import re
import csv

pattern_phone = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)' \
                '(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
new_pattern_phone = r'+7(\3)\6-\8-\10 \12\13'


def get_contact():
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def get_number_phone():
    contacts_list_number = list()
    for contact in contacts_list:
        data = ','.join(contact)
        number = re.sub(pattern_phone, new_pattern_phone, data)
        number_list = number.split(',')
        contacts_list_number.append(number_list)
    return contacts_list_number


def new_contacts_list():
    new_contacts_list = list()
    for contact in contacts_list_number:
        contacts = list()
        name = ",".join(contact[:3])
        result = re.findall(r'(\w+)', name)
        while len(result) < 3:
            result.append('')
        contacts += result
        contacts.append(contact[3])
        contacts.append(contact[4])
        contacts.append(contact[5])
        contacts.append(contact[6])
        new_contacts_list.append(contacts)
    return new_contacts_list


def del_dubl_contacts():
    new_phonebook = []
    for i in range(len(new_contacts_list)):
        for j in range(len(new_contacts_list)):
            if new_contacts_list[i][0] == new_contacts_list[j][0]:
                new_contacts_list[i] = [a or b for a, b in zip(new_contacts_list[i], new_contacts_list[j])]
        if new_contacts_list[i] not in new_phonebook:
            new_phonebook.append(new_contacts_list[i])
    pprint(new_phonebook)
    return new_phonebook


def write_new_phonebook(new_phonebook):
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_phonebook)


if __name__ == '__main__':
    contacts_list = get_contact()
    contacts_list_number = get_number_phone()
    new_contacts_list = new_contacts_list()
    new_phonebook = del_dubl_contacts()
    write_new_phonebook(new_phonebook)

style = ['dr.', 'mr.', 'ms.']
last_name = ['einstein', 'obama', 'mandella', 'obama']
#print("Dr. Einstein is unable to attend the dinner and so we need to replace him.\n")
last_name[0] = 'freeland'
#print("We found a larger dinner table so will invite 3 more guests.")
last_name.insert(0, 'gandi')
last_name.insert(2, 'notley')
last_name.insert(6, 'plante')
print(last_name)
#print("Dear " + style[1].title() + " " + last_name[0].title() + "," +
#      "\n\nPlease accept my invitation to come to dinner on November 24th at 6PM.\n\nYours truly,\n\nPaul Shay\n")
#print("Dear " + style[2].title() + " " + last_name[1].title() + "," +
#      "\n\nPlease accept my invitation to come to dinner on November 24th at 6PM." +
#      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
#print("Dear " + style[2].title() + " " + last_name[2].title() + "," +
#      "\n\nPlease accept my invitation to come to dinner on November 24th at 6PM." +
#      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
#print("Dear " + style[1].title() + " " + last_name[3].title() + "," +
#      "\n\nPlease accept my invitation to come to dinner on November 24th at 6PM." +
#      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
#print("Dear " + style[1].title() + " " + last_name[4].title() + "," +
#      "\n\nPlease accept my invitation to come to dinner on November 24th at 6PM." +
#      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
#print("Dear " + style[2].title() + " " + last_name[5].title() + "," +
#      "\n\nPlease accept my invitation to come to dinner on November 24th at 6PM." +
#      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
#print("Dear " + style[2].title() + " " + last_name[6].title() + "," +
#      "\n\nPlease accept my invitation to come to dinner on November 24th at 6PM." +
#      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
print("Unfortunately the table did not arrive and we can only host two guests for dinner.")
popped_last_name = last_name.pop()
print("Dear " + style[2].title() + " " + popped_last_name.title() + "," +
      "\n\nI am so sorry to inform you that due to logistical problems with the dining room I will not be able to \
host you for dinner after all on November 24th at 6PM. Please accept my sincere apology." +
      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
popped_last_name = last_name.pop()
print("Dear " + style[2].title() + " " + popped_last_name.title() + "," +
      "\n\nI am so sorry to inform you that due to logistical problems with the dining room I will not be able to \
host you for dinner after all on November 24th at 6PM. Please accept my sincere apology." +
      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
popped_last_name = last_name.pop()
print("Dear " + style[1].title() + " " + popped_last_name.title() + "," +
      "\n\nI am so sorry to inform you that due to logistical problems with the dining room I will not be able to \
host you for dinner after all on November 24th at 6PM. Please accept my sincere apology." +
      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
popped_last_name = last_name.pop()
print("Dear " + style[1].title() + " " + popped_last_name.title() + "," +
      "\n\nI am so sorry to inform you that due to logistical problems with the dining room I will not be able to \
host you for dinner after all on November 24th at 6PM. Please accept my sincere apology." +
      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
popped_last_name = last_name.pop()
print("Dear " + style[2].title() + " " + popped_last_name.title() + "," +
      "\n\nI am so sorry to inform you that due to logistical problems with the dining room I will not be able to \
host you for dinner after all on November 24th at 6PM. Please accept my sincere apology." +
      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
print(last_name)
print("Dear " + style[1].title() + " " + last_name[0].title() + "," +
      "\n\nI am so sorry to inform you that due to logistical problems with the dining room I will not be able to \
invite as many people as planned for dinner on November 24th at 6PM but I want to reassure you that you are still \
invited." +
      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
print("Dear " + style[2].title() + " " + last_name[1].title() + "," +
      "\n\nI am so sorry to inform you that due to logistical problems with the dining room I will not be able to \
invite as many people as planned for dinner on November 24th at 6PM but I want to reassure you that you are still \
invited." +
      "\n\nYours truly," + "\n\nPaul Shay" + "\n")
del last_name[1]
del last_name[0]
print (last_name)




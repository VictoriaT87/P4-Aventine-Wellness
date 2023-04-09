
## Manual Testing

This table shows all the manual testing done for the website, and whether it worked as expected or not.

### Features

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
NavBar responsiveness | NavBar becomes hamburger menu on page resize | As expected | Pass
Images resize on mobile | Images resize on mobile | As expected | Pass
Layout becomes linear on mobile | Layout becomes linear on mobile | As expected | Pass
Buttons change colour on hover | Buttons change colour on hover | As expected | Pass
Messages are displayed for user feedback | All messages shown as expected | As expected | Pass
Active menu buttons change for each page | Active menu buttons change for each page | As expected | Pass
Footer links all work when clicked | Footer links all work when clicked | As expected | Pass
Button on home page for users not logged in | button displays "Register to book a session!" | As expected | Pass
Button on home page for users not logged in | button redirects to Sign Up Page | As expected | Pass
Button on home page for users logged in | button displays "Book a session now!" | As expected | Pass
Button on home page for users logged in | button redirects to appointment.html | As expected | Pass
Contact form renders on Contact button | contact.html renders | As expected | Pass
Contact form saves to admin panel | admin panel shows message, name and email | As expected | Pass
User gets feedback on contact form submission | Message "Your message was sent! We'll be in touch shortly." shows | As expected | Pass
Registration page validates each input for empty or whitespaces | message "Please fill in this field is shown" | As expected | Pass
Registration page validates email address | message "A user is already registered with this e-mail address." | As expected | Pass
Registration page validates username | message "A user with that username already exists." | As expected | Pass
Book and Profile links are hidden until a user is logged in | Only show when logged in | As expected | Pass
Book link renders Appointment page | appointments.html is shown | As expected | Pass
Appointments already booked have disabled buttons | buttons are disabled and show "BOOKED" | As expected | Pass
User taken to confirmation page on booking | appointment_confirm_form.html is shown | As expected | Pass
User redirected to appointment page if cancel is clicked on confirm | appointment.html renders on cancel | As expected | Pass
User gets feedback message on booking confirmation | message "Your appointment was successfully booked!" displays | As expected | Pass
Page redirects to profile on booking confirmation | user_profile.html renders on confirmation | As expected | Pass
My Profile link renders Profile page | user_profile.html is shown | As expected | Pass
User information is displayed on Profile page | Username, First Name, Last Name shown | As expected | Pass
User booked appointments shown on Profile page | Appointments shown under "My Booked appointments" | As expected | Pass
Appointments on profile shows message if nothing booked | message "You don't have any saved appointments!" shown | As expected | Pass
Update Account button brings user to update form | user_update.html renders | As expected | Pass
Return button on user_update page redirects back to profile | user_profile.html renders | As expected | Pass
Users updated first name and last name are saved | Profile page updates with new user information | As expected | Pass
Delete Profile button directs to confirmation page | user_delete.html renders | As expected | Pass
Return button on user_delete page redirects back to profile | user_profile.html renders | As expected | Pass
Confirm button on user_delete page redirects back to index.html | index.html renders | As expected | Pass
Confirmation message on user_delete shows | message "Profile successfully deleted" shown | As expected | Pass
All of a users appointments are deleted on profile deletion | appointments removed from database | As expected | Pass
Edit Appointment redirects to update form | edit_appointment form renders | As expected | Pass
Edit Appointment has date widget with restricted days | widget only allows booking up to 6 days ahead | As expected | Pass
Edit Appointment date can be inputted manually | typing a date edits apppointment to that date | As expected | Pass
Edit Appointment timeblock has a dropdown of choices | time choices are shown | As expected | Pass
Delete Appointment redirects to delete confirmation | delete_appointment form renders | As expected | Pass
Delete Appointment cancel button redirects to Profile | user_profile.html renders | As expected | Pass
Delete Appointment delete button redirects to Profile | user_profile.html renders | As expected | Pass
Appointment deleted from database on confirmation | appointment deleted | As expected | Pass
User redirected to logout confirmation when Logout is clicked | account/logout.html renders | As expected | Pass
User redirected to Profile Logout is cancelled | user_profile.html renderes | As expected | Pass
User redirected to Index page when logged out | index.html renderes | As expected | Pass
User shown log out message feedback | message "You have signed out." shown | As expected | Pass

<br>

### Errors

Error Tested | Expected Result | Actual Result | Pass/Fail
-------------|-----------------|---------------|----------
Contact form validates for whitespaces | message "Please fill in this field" shows | As expected | Pass
Book Appointment validates double day booking | message "Cannot schedule more than one appointment on a single day!" shown | As expected | Pass
Edit Appointment validates double day booking | message "Cannot schedule more than one appointment on a single day!" shown | As expected | Pass
Edit Appointment validates double time booking | message "Sorry, this time is already booked!" shown | As expected | Pass
User tried to render user_profile URL when not logged in | user redirected to log in page | As expected | Pass
User tried to render appointment URL when not logged in | user redirected to log in page | As expected | Pass
User tried to render edit_profile URL when not logged in | user redirected to 404 page | As expected | Pass
User tried to render delete_profile URL when not logged in | user redirected to 404 page | As expected | Pass
User tried to render edit_appointment URL when not logged in | user redirected to 404 page | As expected | Pass
User tried to render delete_appointment URL when not logged in | user redirected to 404 page | As expected | Pass
User tried to render user_profile URL for another user | user redirected to 403 page | As expected | Pass
User tried to render appointment URL for another user | user redirected to 403 page | As expected | Pass
User tried to render edit_profile URL for another user | user redirected to 403 page | As expected | Pass
User tried to render delete_profile URL for another user | user redirected to 403 page | As expected | Pass
User tried to render edit_appointment URL for another user | user redirected to 403 page | As expected | Pass
User tried to render delete_appointment URL for another user | user redirected to 403 page | As expected | Pass

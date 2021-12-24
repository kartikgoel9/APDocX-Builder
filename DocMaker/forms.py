from django import forms

from .models import UserCurrentSelectedSubjects, Subject, Experiments




class userCurrentSelectedSubjects(forms.ModelForm):
    class Meta:
        model = UserCurrentSelectedSubjects
        fields = ['selected_subject']
        labels = {

            'selected_subject': 'Subject Name'

        }





class addSubject(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_faculty', 'subject_name', 'semester', 'roll_no']


class addExperiment(forms.ModelForm):
    class Meta:
        model = Experiments
        fields = ['experiment_name','experiment_number', 'aim', 'source_code', 'image_one']
        labels = {

            'experiment_name': 'Subject Name'

        }


class editExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiments
        fields = ['aim', 'source_code']

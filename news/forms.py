from django import forms
from django.core.mail import send_mail
from .models import reviews, Response


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = reviews
        fields = ('name', 'email', 'text_rev', 'vork_user')

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

            # Отправка оповещения на почту
            send_mail(
                'Новый отзыв',
                f'Получен новый отзыв от {instance.name}.',
                'webmaster@example.com',  # Замените на ваш настоящий адрес отправителя
                ['aachkasov2013@gmail.com'],  # Список адресов получателей
                fail_silently=False,
            )
        return instance

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('name_res', 'email_res', 'text_rev_res', 'vork_user_res')

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            print("Ответ на отзыв сохранен успешно!")
            print(f"Имя: {instance.name_res}, Почта: {instance.email_res}, Ответ: {instance.text_rev_res}, Родительский отзыв: {instance.parent_review_res}")
            # Отправка оповещения на почту
            send_mail(
                'Новый ответ на отзыв',
                f'Получен новый ответ на отзыв от {instance.name}.',
                'webmaster@example.com',  # Замените на ваш настоящий адрес отправителя
                ['aachkasov2013@gmail.com'],  # Список адресов получателей
                fail_silently=False,
            )
        return instance



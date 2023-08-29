from rest_framework.response import Response
from rest_framework.views import APIView

from botsessions.models import BotSession
from users.models import CustomUser
from users.serializers import UserSerializer


class ChatBotView(APIView):
    def post(self, request):
        input_data = request.data.get('message')
        session_id = request.data.get('session_id')
        session, created = BotSession.objects.get_or_create(id=session_id)

        if session.step == 0:
            response = "Введите ваш адрес электронной почты:"
            session.step += 1
        elif session.step == 1:
            if CustomUser.objects.filter(email=input_data).exists():
                return Response({"message": "Пользователь с таким адресом уже существует"})
            session.data['email'] = input_data
            response = "Введите ваше ФИО:"
            session.step += 1
        elif session.step == 2:
            session.data['full_name'] = input_data
            response = "Введите ваш номер телефона:"
            session.step += 1
        elif session.step == 3:
            session.data['phone_number'] = input_data
            response = "Введите ваш пароль:"
            session.step += 1
        elif session.step == 4:
            session.data['password'] = input_data
            # В этом месте мы непосредственно регистрируем пользователя
            user_serializer = UserSerializer(data=session.data)
            if user_serializer.is_valid():
                user_serializer.save()
                session.user = user_serializer.instance
                session.save()
                response = "Регистрация успешно завершена!"
                session.step += 1
            else:
                response = "Произошла ошибка при регистрации. Пожалуйста, начните заново."
                session.delete()
        else:
            response = "Сессия завершена."

        session.save()
        return Response({"message": response, "session_id": session.id})

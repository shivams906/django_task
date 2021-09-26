from django.contrib.auth import get_user_model
from rest_framework import fields, serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "address",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

    def create(self, validated_data):
        if "username" in validated_data and validated_data["username"] == "":
            validated_data["username"] = None
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        if "username" in validated_data and validated_data["username"] == "":
            validated_data["username"] = None
        instance = super().update(instance, validated_data)
        if "password" in validated_data:
            instance.set_password(validated_data["passowrd"])
            instance.save()
        return instance

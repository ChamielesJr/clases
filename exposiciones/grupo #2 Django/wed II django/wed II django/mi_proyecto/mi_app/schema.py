import graphene
from graphene_django.types import DjangoObjectType
from .models import Libro

# Tipo GraphQL basado en el modelo Libro
class LibroType(DjangoObjectType):
    class Meta:
        model = Libro

# Consultas
class Query(graphene.ObjectType):
    hola = graphene.String(description="Un saludo")
    libros = graphene.List(LibroType)

    def resolve_hola(root, info):
        return "¡Hola desde GraphQL en Django!"

    def resolve_libros(root, info):
        return Libro.objects.all()

# Crear libro
class CrearLibro(graphene.Mutation):
    class Arguments:
        titulo = graphene.String(required=True)
        autor = graphene.String(required=True)

    libro = graphene.Field(LibroType)

    def mutate(self, info, titulo, autor):
        libro = Libro(titulo=titulo, autor=autor)
        libro.save()
        return CrearLibro(libro=libro)

# Editar libro
class EditarLibro(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        titulo = graphene.String()
        autor = graphene.String()

    libro = graphene.Field(LibroType)

    def mutate(self, info, id, titulo=None, autor=None):
        libro = Libro.objects.get(pk=id)
        if titulo:
            libro.titulo = titulo
        if autor:
            libro.autor = autor
        libro.save()
        return EditarLibro(libro=libro)

# Eliminar libro
class EliminarLibro(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        libro = Libro.objects.get(pk=id)
        libro.delete()
        return EliminarLibro(ok=True)

# Mutaciones agrupadas
class Mutation(graphene.ObjectType):
    crear_libro = CrearLibro.Field()
    editar_libro = EditarLibro.Field()
    eliminar_libro = EliminarLibro.Field()

# Esquema final
schema = graphene.Schema(query=Query, mutation=Mutation)

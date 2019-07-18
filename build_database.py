import database_builders.ksu as ksu_builder
import lib.db.table_model_generator as table_model_generator

def build():
    ksu_builder.build()
    table_model_generator.generate_models()
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase_url = os.getenv ('SUPABASE_URL')
supabase_key = os.getenv ('SUPABASE_KEY')

supabase = create_client(supabase_url,supabase_key)

resposta = (supabase.table('pedidos')
            .select('id,valor,forma_pagamento,usuarios(nome)')
            .eq('id_usuario',1)
            .execute())
print(resposta.data)



test_scenarios_parser = [
    (
        '<rss><channel> <item>'
        '   <title>Title</title>'
        '   <link>URL Link</link>'
        '   <description><![CDATA['
        '       <p>P Content</p>'
        '   ]]</description>'
        '</item> </channel></rss>',
        {
            'feed': [
                 {
                    'title': 'Title',
                    'link': 'URL Link',
                    'description': [
                        {
                            'type': 'text',
                            'content': 'P Content'
                        },
                    ]
                 },
            ]
        }
    ),
    # (
    #     '<rss><channel> <item>'
    #     '   <title>Title</title>'
    #     '   <link>URL Link</link>'
    #     '   <description>'
    #     '       <div><img src=\'www.google.com\'/></div>'
    #     '   </description>'
    #     '</item> </channel></rss>',
    #     {
    #         'feed': [
    #              {
    #                 'title': 'Title',
    #                 'link': 'URL Link',
    #                 'description': [
    #                     {
    #                         'type': 'image',
    #                         'content': 'www.google.com'
    #                     },
    #                 ]
    #              },
    #         ]
    #     }
    # ),
    # (
    #     '<rss><channel> <item>'
    #     '   <title>Title</title>'
    #     '   <link>URL Link</link>'
    #     '   <description>'
    #     '       <div><ul>'
    #     '           <li><a href=\'www.link1.com\'/></li>'
    #     '           <li><a href=\'www.link2.com\'/></li>'
    #     '           <li><a href=\'www.link3.com\'/></li>'
    #     '       </ul></div>'
    #     '   </description>'
    #     '</item> </channel></rss>',
    #     {
    #         'feed': [
    #              {
    #                 'title': 'Title',
    #                 'link': 'URL Link',
    #                 'description': [
    #                     {
    #                         'type': 'links',
    #                         'content': [
    #                             'www.link1.com',
    #                             'www.link2.com',
    #                             'www.link3.com'
    #                         ]
    #                     }
    #                 ]
    #              },
    #         ]
    #     }
    # ),
    # (
    #     '<rss><channel> <item>'
    #     '   <title>Title</title>'
    #     '   <link>URL Link</link>'
    #     '   <description>'
    #     '       <div><ul>'
    #     '           <li><a href=\'www.link1.com\'/></li>'
    #     '           <li><a href=\'www.link2.com\'/></li>'
    #     '       </ul></div>'
    #     '       <p>P Content</p>'
    #     '       <div><img src=\'www.google.com\'/></div>'
    #     '   </description>'
    #     '</item> </channel></rss>',
    #     {
    #         'feed': [
    #              {
    #                 'title': 'Title',
    #                 'link': 'URL Link',
    #                 'description': [
    #                     {
    #                         'content': 'P Content',
    #                         'type': 'text',
    #                     },
    #                     {
    #                         'content': ['www.link1.com', 'www.link2.com'],
    #                         'type': 'links',
    #                     },
    #                     {
    #                         'content': 'www.google.com',
    #                         'type': 'image',
    #
    #                     },
    #                 ]
    #              },
    #         ]
    #     }
    # ),
]

test_scenarios_items_elements = [
    ('<rss><channel></channel></rss>', 0),
    ('<rss><channel> <item></item> <item></item> </channel></rss>', 2)
]

feed_input_file_expected_json = {'feed': [{
   "title": "Volkswagen Arteon aparece às vésperas do Salão de Genebra",
   "link": "http://revistaautoesporte.globo.com/Noticias/noticia/2017/03/volkswagen-arteon-aparece-vesperas-do-salao-de-genebra.html",
   "description": [
      {
         "type": "image",
         "content": "http://s2.glbimg.com/DIgFxpN0aAu99uvuZ3WmSqAUV2E=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/1_WKIn5xh.jpg"
      },
      {
         "type": "text",
         "content": "A Volkswagen revelou hoje (6) o Arteon, cupê de quatro portas escolhido para suceder o CC – antes chamado Passat CC – e que será apresentado ao público durante o Salão de Genebra. O visual não chega a ser novidade, já que é praticamente o mesmo há dois anos, quando deu as caras no evento suíço como o protótipo Sport Coupé GTE Concept."
      },
      {
         "type": "image",
         "content": "http://s2.glbimg.com/NgWcluzNZLlXwCu9Vs8N1UHXGbI=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/2_aEXyzmK.jpg"
      },
      {
         "type": "text",
         "content": "Para encarar o mundo real, a novidade recebeu maçanetas nas portas, antena no teto e alguns detalhes exigidos por lei... e só! Até mesmo as rodas gigantes, os para-choques agressivos e a grade do motor integrada aos faróis continuam ali – para a alegria dos fãs. Além do pacote esportivo R-Line, também haverá opções um pouco mais conservadoras."
      },
      {
         "type": "image",
         "content": "http://s2.glbimg.com/lJKzhfcrbXSzQZRKXCcn7pEIRjw=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/3_BZIDgsI.jpg"
      },
      {
         "type": "text",
         "content": "Se por fora tudo é diferente (e muito mais agressivo) comparado aos “irmãos”, o painel segue fiel ao estilo da marca – afinal, é o mesmo do Passat. Não sabemos se a queda do teto compromete o espaço para a cabeça de quem vai atrás, mas os 563 litros do porta-malas são bem aproveitados graças à tampa traseira que abre com o vidro, como um hatch."
      },
      {
         "type": "image",
         "content": "http://s2.glbimg.com/RJ9LxS8YaH4bCAlP1f_1Nm8cocY=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/4_vYYIbul.jpg"
      },
      {
         "type": "text",
         "content": "A plataforma é a mesma MQB utilizada no Passat (que, graças ao milagre da modularidade, também serve ao Golf e, futuramente, à nova geração do Gol nacional). São 4,86 metros de comprimento; 1,87 m de largura; 1,42 m de altura; e 2,84 m de entre-eixos. Ainda que pareça um latifúndio, apenas quatro ocupantes viajam com conforto na cabine."
      },
      {
         "type": "image",
         "content": "http://s2.glbimg.com/EDuoev-xcbKnAK_QVWRclJa4Mac=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/5_71gviOe.jpg"
      },
      {
         "type": "text",
         "content": "No Velho Continente, serão oferecidos motores a gasolina (1.5 turbo com 150 cv e 2.0 turbo nas opções de 190 cv e 280 cv) e também a diesel (2.0 turbo nas opções de 150 cv, 190 cv e 240 cv). Com exceção das versões de entrada, que têm câmbio manual de seis marchas, a transmissão é sempre automatizada com dupla embreagem e sete marchas."
      },
      {
         "type": "links",
         "content": [
            "http://revistaautoesporte.globo.com/Noticias/noticia/2016/01/os-12-mimos-mais-legais-do-volkswagen-passat.html",
            "http://revistaautoesporte.globo.com/Analises/noticia/2015/11/avaliacao-novo-volkswagen-passat.html"
         ]
      },
      {
         "type": "image",
         "content": "http://s2.glbimg.com/fkJMyLGJsX_ThzJBHalbemmcb4M=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/6_pih5QJE.jpg"
      }
   ]}]
}

test_scenarios_is_authenticated = {
    ('', False),
    ('http://localhost:6543/', False),
    ('http://localhost:6543/login/', True)
}

from goods.models import Products
#from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

def q_search(query):
    if query.isdigit() and len(query)<=5:
        return Products.objects.filter(id=int(query))

    #return Products.objects.filter(description__search=query)
    #return Products.objects.annotate(search=SearchVector("title", "description"),).filter(search=query)
    vector=SearchVector("title", "description")
    query=SearchQuery(query)
    #return Products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")
    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "title",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    return result



    # keywords=[word for word in query.split() if len(word)>2]
    # q_objects=Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(title__icontains=token)

    # return Products.objects.filter(q_objects)
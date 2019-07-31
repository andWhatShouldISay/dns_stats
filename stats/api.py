from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from stats.models import Domain_stats,Company,User,Domain
from django.db.models import Q




class statsAuthorization(Authorization):
    def read_list(self, object_list, bundle):
	username = bundle.request.session.get('username','')
	if username == '':
        	raise Unauthorized("Not authorized.")
	allowed_domains = [domain.__str__() for domain in Domain.objects.filter(companyid = User.objects.get(username = username).companyid)]
		
        return object_list.filter(qname__in=allowed_domains)

    def read_detail(self, object_list, bundle):
        return True

    def create_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no creates.")

    def create_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no creates.")

    def update_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no updates.")

    def update_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no updates.")

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")


class DomainStatsResource(ModelResource):
    class Meta:
        queryset = Domain_stats.objects.all()
        resource_name = 'Domain_stats'
	filtering = {"qname" : ('exact')}
	authorization = statsAuthorization()
        

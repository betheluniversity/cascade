/*
 * Created on Aug 19, 2007 by Mike Strauch
 * 
 * Copyright(c) 2006 Hannon Hill Corporation. All rights reserved.
 */
package com.hannonhill.cascade.config.hibernate.event;

import org.hibernate.HibernateException;
import org.hibernate.event.DeleteEvent;
import org.hibernate.event.def.DefaultDeleteEventListener;

import com.hannonhill.cascade.cache.discarder.BaseCacheDiscarder;
import com.hannonhill.cascade.cache.discarder.CacheDiscarderProvider;
import com.hannonhill.cascade.model.dom.BaseDomainObject;
import com.hannonhill.cascade.model.dom.CascadeDomainObject;
import com.hannonhill.cascade.model.dom.identifier.EntityIdentifierFactory;
import com.hannonhill.cascade.model.dom.identifier.EntityTypeUtil;
import com.hannonhill.cascade.model.service.ServiceProvider;

/**
 * Hibernate event listener that handles delete events.
 * 
 * @author Mike Strauch
 * @since 5.0
 */
public class CascadeDeleteEntityListener extends DefaultDeleteEventListener
{
    private static final long serialVersionUID = -1833948095560381783L;
    private CacheDiscarderProvider cacheDiscarderProvider;
    private ServiceProvider serviceProvider;

    @Override
    public void onDelete(DeleteEvent event) throws HibernateException
    {
        super.onDelete(event);

        Object obj = event.getObject();

        if (EntityTypeUtil.isSearchable(obj))
        {
            serviceProvider.getSearchService().remove(
                    EntityIdentifierFactory.createIdentifier(((BaseDomainObject) obj).getId(), ((BaseDomainObject) obj).getType()));
        }

        if (obj instanceof CascadeDomainObject)
        {
            CascadeDomainObject dom = (CascadeDomainObject) obj;
            BaseCacheDiscarder discarder = cacheDiscarderProvider.getCacheDiscarder(dom.getType());
            if (discarder != null)
                discarder.discardFromCacheOnDelete(dom);
        }
    }

    /**
     * @param cacheDiscarderProvider the cacheDiscarderProvider to set
     */
    public void setCacheDiscarderProvider(CacheDiscarderProvider cacheDiscarderProvider)
    {
        this.cacheDiscarderProvider = cacheDiscarderProvider;
    }

    /**
     * @param serviceProvider the serviceProvider to set
     */
    public void setServiceProvider(ServiceProvider serviceProvider)
    {
        this.serviceProvider = serviceProvider;
    }
}

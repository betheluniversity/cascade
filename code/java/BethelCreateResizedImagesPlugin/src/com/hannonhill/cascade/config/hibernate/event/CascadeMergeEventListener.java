/*
 * Created on Aug 19, 2007 by Mike Strauch
 * 
 * Copyright(c) 2006 Hannon Hill Corporation. All rights reserved.
 */
package com.hannonhill.cascade.config.hibernate.event;

import org.hibernate.HibernateException;
import org.hibernate.event.MergeEvent;
import org.hibernate.event.def.DefaultMergeEventListener;

import com.hannonhill.cascade.model.dom.BaseDomainObject;
import com.hannonhill.cascade.model.dom.identifier.EntityIdentifierFactory;
import com.hannonhill.cascade.model.dom.identifier.EntityTypeUtil;
import com.hannonhill.cascade.model.service.ServiceProvider;

/**
 * Hibernate event listener that handles merge events.
 * 
 * @author Mike Strauch
 * @since 5.0
 */
public class CascadeMergeEventListener extends DefaultMergeEventListener
{
    private static final long serialVersionUID = 5195399834297133707L;

    private ServiceProvider serviceProvider;

    @Override
    public void onMerge(MergeEvent event) throws HibernateException
    {
        super.onMerge(event);

        Object obj = event.getEntity();

        if (EntityTypeUtil.isSearchable(obj))
        {
            serviceProvider.getSearchService().update(
                    EntityIdentifierFactory.createIdentifier(((BaseDomainObject) obj).getId(), ((BaseDomainObject) obj).getType()));
        }
    }

    /**
     * @param serviceProvider the serviceProvider to set
     */
    public void setServiceProvider(ServiceProvider serviceProvider)
    {
        this.serviceProvider = serviceProvider;
    }
}

/*
 * Created on Aug 19, 2007 by Mike Strauch
 * 
 * Copyright(c) 2006 Hannon Hill Corporation. All rights reserved.
 */
package com.hannonhill.cascade.config.hibernate.event;

import org.hibernate.event.SaveOrUpdateEvent;
import org.hibernate.event.def.DefaultSaveOrUpdateEventListener;

import com.hannonhill.cascade.model.dom.BaseDomainObject;
import com.hannonhill.cascade.model.dom.identifier.EntityIdentifierFactory;
import com.hannonhill.cascade.model.dom.identifier.EntityTypeUtil;
import com.hannonhill.cascade.model.service.ServiceProvider;

/**
 * Hibernate event listener that handles update events.
 * 
 * @author Mike Strauch
 * @since 5.0
 */
public class CascadeSaveEventListener extends DefaultSaveOrUpdateEventListener
{
    private static final long serialVersionUID = -7520904402683423680L;

    private ServiceProvider serviceProvider;

    @Override
    public void onSaveOrUpdate(SaveOrUpdateEvent event)
    {
        super.onSaveOrUpdate(event);

        Object obj = event.getObject();

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

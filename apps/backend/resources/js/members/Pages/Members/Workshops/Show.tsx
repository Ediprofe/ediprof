import AssignmentDetailPage from '../../../Components/AssignmentDetailPage';
import type { MemberAssignment } from '../../../types';

type WorkshopShowProps = {
    pageTitle: string;
    subtitle?: string;
    workshop: MemberAssignment;
};

export default function WorkshopShow({ pageTitle, subtitle, workshop }: WorkshopShowProps) {
    return (
        <AssignmentDetailPage
            pageTitle={pageTitle}
            subtitle={subtitle}
            assignment={workshop}
            section="workshops"
        />
    );
}
